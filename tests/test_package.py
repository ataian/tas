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
    "references/skill-mechanics.md", "third_party/mattpocock/LICENSE",
    "third_party/caveman/LICENSE-MIT", "third_party/caveman/NOTICE",
    "third_party/caveman/LICENSING.md", "third_party/generic-devteam/LICENSE",
    "tests/test_package.py",
}


METHOD_CONTRACTS = {
    "Context pointers": ("state what the target contains", "one trigger per distinct branch",
                         "Sharpen a weak pointer before inlining"),
    "The two loads": ("Context load", "Cognitive load", "human judgement"),
    "Information hierarchy": ("In-file steps", "In-file reference", "Disclosed reference",
                              "Inline what every branch needs", "Co-locate", "Sprawl"),
    "Steps and completion": ("checkable and exhaustive", "Sharpen the criterion first",
                             "observe premature completion", "real context boundary"),
    "Leading words and positive prompting": ("established semantic anchors", "execution",
                                            "invocation", "positive target", "hard guardrails"),
    "Pruning": ("single source of truth", "environment", "reasons, conventions, and gotchas",
                "sediment", "model-relative", "actual runs"),
}


def validate_method(root):
    """Static instruction contracts; mutation coverage is not model-behavior evidence."""
    standard = (root / "references/tas-authoring-standard.md").read_text(encoding="utf-8")
    for heading, clauses in METHOD_CONTRACTS.items():
        section = re.search(r"^## " + re.escape(heading) + r"\n(.*?)(?=^## |\Z)",
                            standard, re.MULTILINE | re.DOTALL)
        assert section, f"missing method section: {heading}"
        for clause in clauses:
            assert clause in section[1], f"missing method instruction: {heading}: {clause}"
    assert "For ticket bodies, use short statements" in standard, "ticket-only output scope"
    assert "Include concise story criteria and necessary technical context" in standard, "accepted ticket policy"
    assert "English for development communication and artifacts" in standard, "development language"
    mechanics = (root / "references/skill-mechanics.md").read_text(encoding="utf-8")
    for clause in ("model-invoked", "user-invoked", "disable-model-invocation: true",
                   "verified", "catalog", "does not establish", "plain reference",
                   "Splitting by invocation", "Router"):
        assert clause in mechanics, f"missing invocation contract: {clause}"
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    assert "When the commissioned text is a skill" in skill, "missing skill branch trigger"
    assert "references/skill-mechanics.md" in skill, "missing skill mechanics pointer"


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
    for field in ("name: tas", "version: 1.1.0", "license: MIT"):
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

    for relative in ("references/caveman.md", "references/caveman-review.md"):
        text = (root / relative).read_text(encoding="utf-8")
        assert not text.startswith("---\n"), f"style reference has skill metadata: {relative}"
        assert not re.search(
            r"ultracave|megacave|/caveman\b|^## Persistence$|stop caveman|normal mode",
            text, re.IGNORECASE | re.MULTILINE,
        ), f"unsupported style routing: {relative}"

    sources = json.loads((root / "sources.json").read_text(encoding="utf-8"))
    assert sources["package_version"] == "1.1.0", "source version"
    originals = sources["upstream_files"]
    assert {entry["local_path"] for entry in originals} == {
        "references/caveman.md", "references/caveman-review.md",
        "third_party/caveman/LICENSE", "third_party/caveman/LICENSE-MIT",
        "third_party/caveman/NOTICE", "third_party/caveman/LICENSING.md",
        "third_party/generic-devteam/LICENSE",
        "third_party/mattpocock/LICENSE",
    }, "upstream file coverage"
    for entry in originals:
        assert entry["local_path"] in PUBLIC_FILES, "undeclared source destination"
        actual = hashlib.sha256((root / entry["local_path"]).read_bytes()).hexdigest()
        assert actual == entry["sha256"], f"source bytes changed: {entry['local_path']}"
    validate_method(root)
    method_source = sources["writing_for_agents"]
    assert method_source["repository"] == "https://github.com/mattpocock/skills", "method repository"
    assert re.fullmatch(r"[0-9a-f]{40}", method_source["revision"]), "method revision"
    assert {entry["source_path"] for entry in method_source["source_files"]} == {
        "skills/productivity/writing-for-agents/SKILL.md",
        "skills/productivity/writing-for-agents/SKILL-MECHANICS.md",
        "skills/productivity/writing-for-agents/agents/openai.yaml",
    }, "complete original method inventory"
    for entry in method_source["source_files"]:
        assert re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]), "method original hash"
    for relative, expected in method_source["adapted_files"].items():
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == expected, "adapted method bytes"
    standard = (root / "references/tas-authoring-standard.md").read_bytes()
    assert hashlib.sha256(standard).hexdigest() == sources["tas"]["packaged_sha256"], "TAS bytes changed"
    assert "integrations.md" not in standard.decode(), "external Maker reference"
    return True


class PackageTests(unittest.TestCase):
    def test_writing_method_preserves_portable_contracts(self):
        validate_method(ROOT)

    def test_empty_method_body_is_rejected_with_heading_retained(self):
        for heading in METHOD_CONTRACTS:
            with self.subTest(section=heading):
                root = self.copy_package()
                path = root / "references/tas-authoring-standard.md"
                path.write_text(re.sub(
                    r"(^## " + re.escape(heading) + r"\n).*?(?=^## |\Z)",
                    r"\1\n", path.read_text(), flags=re.MULTILINE | re.DOTALL), encoding="utf-8")
                with self.assertRaisesRegex(AssertionError, "missing method instruction"):
                    validate_method(root)

    def test_removed_skill_branch_is_rejected(self):
        root = self.copy_package()
        path = root / "SKILL.md"
        path.write_text(path.read_text().replace("When the commissioned text is a skill", "For any text"))
        with self.assertRaisesRegex(AssertionError, "missing skill branch trigger"):
            validate_method(root)

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

    def test_style_references_have_no_skill_metadata_or_mode_routing(self):
        for relative in ("references/caveman.md", "references/caveman-review.md"):
            with self.subTest(reference=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertFalse(text.startswith("---\n"), "style reference has skill metadata")
                self.assertNotRegex(text, r"(?im)ultracave|megacave|/caveman\b|^## Persistence$|stop caveman|normal mode")

    def test_skill_command_in_style_reference_is_rejected(self):
        root = self.copy_package()
        path = root / "references/caveman-review.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nUse /caveman-review.\n", encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "unsupported style routing"):
            validate_package(root)

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
