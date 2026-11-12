"""Offline package-contract checks. These do not measure agent behavior."""

import hashlib
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = {
    ".gitignore", "LICENSE", "NOTICE.md", "README.md", "SKILL.md", "sources.json",
    "references/tas-authoring-standard.md", "references/caveman.md",
    "references/caveman-review.md", "third_party/caveman/LICENSE",
    "third_party/caveman/LICENSE-MIT", "third_party/caveman/NOTICE",
    "third_party/caveman/LICENSING.md", "third_party/generic-devteam/LICENSE",
    "tests/test_package.py",
}


def validate_package(root):
    """Validate declared contents, local links, source bytes, and loading contracts."""
    root = root.resolve()
    for relative in sorted(PUBLIC_FILES):
        path = root / relative
        assert path.is_file(), f"missing public file: {relative}"
        assert not path.is_symlink(), f"symlink: {relative}"
        assert path.resolve().is_relative_to(root), f"escaping path: {relative}"

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\n"), "frontmatter opening"
    header, body = skill[4:].split("\n---\n", 1)
    for field in ("name: tas", "version: 1.0.0", "license: MIT"):
        assert field in header.splitlines(), f"frontmatter field: {field}"
    description = re.search(r"^description: (.+)$", header, re.MULTILINE)
    assert description and len(description[1]) <= 60, "description length"
    assert description[1].endswith("."), "description punctuation"
    for clause in (
        "on every invocation", "references/tas-authoring-standard.md",
        "references/caveman.md", "references/caveman-review.md",
        "missing or unreadable", "assigned review procedure",
    ):
        assert clause in body, f"missing loading contract: {clause}"

    for relative in sorted(PUBLIC_FILES):
        if not relative.endswith(".md"):
            continue
        text = (root / relative).read_text(encoding="utf-8")
        assert not re.search(r"/(?:home|Users)/[^\s`]+", text), f"private path: {relative}"
        for destination in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            link = urlsplit(destination)
            if link.scheme or link.netloc:
                continue
            linked = ((root / relative).parent / unquote(link.path)).resolve()
            assert linked.is_relative_to(root), f"escaping link: {relative}: {destination}"
            assert linked.is_file(), f"missing local link: {relative}: {destination}"
            if link.fragment:
                headings = re.findall(r"^#+\s+(.+)$", linked.read_text(encoding="utf-8"), re.MULTILINE)
                anchors = {re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-") for h in headings}
                assert unquote(link.fragment) in anchors, f"missing anchor: {destination}"

    sources = json.loads((root / "sources.json").read_text(encoding="utf-8"))
    assert sources["package_version"] == "1.0.0", "source version"
    originals = sources["upstream_files"]
    assert {entry["local_path"] for entry in originals} == {
        "references/caveman.md", "references/caveman-review.md",
        "third_party/caveman/LICENSE", "third_party/caveman/LICENSE-MIT",
        "third_party/caveman/NOTICE", "third_party/caveman/LICENSING.md",
        "third_party/generic-devteam/LICENSE",
    }, "upstream file coverage"
    for entry in originals:
        assert entry["local_path"] in PUBLIC_FILES, "undeclared source destination"
        actual = hashlib.sha256((root / entry["local_path"]).read_bytes()).hexdigest()
        assert actual == entry["sha256"], f"source bytes changed: {entry['local_path']}"
    standard = (root / "references/tas-authoring-standard.md").read_bytes()
    assert hashlib.sha256(standard).hexdigest() == sources["tas"]["packaged_sha256"], "TAS bytes changed"
    assert "integrations.md" not in standard.decode(), "external Maker reference"
    return True


class PackageTests(unittest.TestCase):
    def copy_package(self):
        temporary = tempfile.TemporaryDirectory(prefix="tas-package-")
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        for relative in PUBLIC_FILES:
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)
        return root

    def test_package_contract(self):
        self.assertTrue(validate_package(ROOT))

    def test_relocated_package_needs_no_maker_or_network(self):
        self.assertTrue(validate_package(self.copy_package()))

    def test_missing_reference_is_rejected(self):
        root = self.copy_package()
        (root / "references/caveman-review.md").unlink()
        with self.assertRaisesRegex(AssertionError, "missing public file"):
            validate_package(root)

    def test_changed_upstream_reference_is_rejected(self):
        root = self.copy_package()
        path = root / "references/caveman.md"
        path.write_bytes(path.read_bytes() + b"\nchanged\n")
        with self.assertRaisesRegex(AssertionError, "source bytes changed"):
            validate_package(root)

    def test_escaping_reference_is_rejected(self):
        root = self.copy_package()
        path = root / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[Escape](../../outside.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "escaping link"):
            validate_package(root)

    def test_removed_loading_instruction_is_rejected(self):
        root = self.copy_package()
        path = root / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("on every invocation", "when convenient"), encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "missing loading contract"):
            validate_package(root)


if __name__ == "__main__":
    unittest.main()
