# Attribution and adaptations

## TAS

TAS means Technical Agent Specification. The standard derives from the `generic-devteam` project's `references/tas-authoring-standard.md`, by Max and the generic-devteam contributors.
The original MIT notice is retained in [third_party/generic-devteam/LICENSE](third_party/generic-devteam/LICENSE).
[Sources and checksums](sources.json) identify the historical source snapshot, the later accepted Maker baseline, method sources, and bundled files.

The initial standalone adaptation localized the style-source links and made consumer loading explicit.
The maintained standard now integrates writing-for-agents and preserves the accepted Maker ticket policy, including the ticket-only scope of its short-bullet rule.
Both style links resolve to bundled TAS adaptations. Other roles must load their TAS instructions explicitly.
The new entrypoint, README, checks, and provenance inventory package this standard independently of the Maker.

## Writing-for-agents

The standard and [Skill mechanics](references/skill-mechanics.md) adapt Matt Pocock's `writing-for-agents/SKILL.md` and required `SKILL-MECHANICS.md` at the exact revision in `sources.json`.
The complete originals and `agents/openai.yaml` were inspected; their source paths and hashes remain recorded for comparison.
These are TAS adaptations, not bundled original skill trees or an installation of writing-for-agents.
The original [MIT license](third_party/mattpocock/LICENSE), Copyright (c) 2026 Matt Pocock, is retained unchanged.

The adaptation integrates context pointers, the two loads, information hierarchy, completion clarity/demand, leading words, positive prompting, and pruning with TAS authority and evidence contracts.
Skill invocation, explicit-only metadata, and router mechanics are conditional on verified harness behaviour.
The original's `disable-model-invocation: true` semantics are not asserted as a portable capability.
Behavioural explanations guide authoring; no model benchmark, compliance improvement, or token saving is claimed by these package checks.

## Caveman

The package adapts `skills/caveman/SKILL.md` and `skills/caveman-review/SKILL.md` from Julius Brussee's Caveman project.
The instruction files are renamed to ordinary references. Skill metadata, session persistence, hook/status handling, alternate-mode routing, and activation/deactivation commands are removed.
The remaining writing rules and Auto-Clarity guidance are retained. The source inventory records original and packaged checksums separately.
Caveman is a third-party style source, not the author or sponsor of TAS.

Copyright 2026 Julius Brussee.
The selected release uses Apache-2.0. Earlier MIT-covered contributions retain their original notice.
The original [LICENSE](third_party/caveman/LICENSE), [LICENSE-MIT](third_party/caveman/LICENSE-MIT), [NOTICE](third_party/caveman/NOTICE), and [LICENSING.md](third_party/caveman/LICENSING.md) are retained unchanged.

The upstream notice and licensing explanation describe the broader Caveman distribution.
This package bundles only its two instruction files and legal documents, not its CLI, engine, hooks, fonts, proxy, cloud service, or mode-management system.
Descriptive upstream paths inside the retained legal documents refer to that upstream distribution, not required TAS files.
