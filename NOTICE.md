# Attribution and adaptations

## TAS

TAS means Technical Agent Specification. The standard derives from the `generic-devteam` project's `references/tas-authoring-standard.md`, by Max and the generic-devteam contributors.
The original MIT notice is retained in [third_party/generic-devteam/LICENSE](third_party/generic-devteam/LICENSE).
[Sources and checksums](sources.json) identify source revisions, the TAS working-tree snapshot, and bundled files.

The standalone adaptation changes only the standard's style-source links and its Maker-specific generated-role loading statement.
Both style links now resolve to bundled originals. Other roles must load their TAS instructions explicitly.
All other source-standard wording remains unchanged.
The new entrypoint, README, checks, and provenance inventory package this standard independently of the Maker.

## Caveman

The package includes the original `skills/caveman/SKILL.md` and `skills/caveman-review/SKILL.md` from Julius Brussee's Caveman project.
They are renamed to ordinary reference files without changing their bytes.
Caveman is a third-party style source, not the author or sponsor of TAS.

Copyright 2026 Julius Brussee.
The selected release uses Apache-2.0. Earlier MIT-covered contributions retain their original notice.
The original [LICENSE](third_party/caveman/LICENSE), [LICENSE-MIT](third_party/caveman/LICENSE-MIT), [NOTICE](third_party/caveman/NOTICE), and [LICENSING.md](third_party/caveman/LICENSING.md) are retained unchanged.

The upstream notice and licensing explanation describe the broader Caveman distribution.
This package bundles only its two instruction files and legal documents, not its CLI, engine, hooks, fonts, proxy, cloud service, or mode-management system.
Descriptive upstream paths inside the retained legal documents refer to that upstream distribution, not required TAS files.
