# TAS — Technical Agent Specification

A standalone skill for concise, precise agent instructions. TAS combines Matt Pocock's writing-for-agents method with authority, conditions, approval gates, technical details, and verifiable outcomes.

## Use from a checkout

Give your agent the path to this repository's `SKILL.md`:

> Read `./SKILL.md` and its required local references. Apply TAS to `./AGENTS.md`. Preserve authority, conditions, exceptions, and approval gates. Change only the commissioned text.

Resolve `./SKILL.md` against this checkout. Resolve the target file against the project you commissioned.
Reading the skill and authorizing a file edit are separate actions.

## Install as a skill

Register the complete repository directory as `tas` through your agent's supported local-skill mechanism.
Keep `SKILL.md`, `references/`, and `third_party/` together; copying only the entrypoint is incomplete.
If another skill named `tas` exists, select the intended implementation before installation rather than merging them.

The skill uses file-reading capabilities, not a particular agent API. It needs no Maker checkout, Caveman runtime, API key, package installation, or network access during use.

## Included files

- [SKILL.md](SKILL.md): triggers, loading procedure, scope, and verification.
- [TAS standard](references/tas-authoring-standard.md): instruction, compression, placement, and output contracts.
- [Skill mechanics](references/skill-mechanics.md): skill-only invocation design, conditional harness mechanisms, and invocation splits.
- [Caveman](references/caveman.md): TAS-adapted writing-style reference.
- [Caveman Review](references/caveman-review.md): TAS-adapted findings format with Auto-Clarity.
- [Source inventory](sources.json): pinned origins and checksums.
- [Attribution and adaptations](NOTICE.md): license boundaries and changes from the source standard.

The Caveman instruction files are bundled as style references, with skill metadata and runtime mode handling removed.
The assigned review process remains responsible for tests and verdicts.
TAS applies the writing style to persisted text too; clarity, safety warnings, conditions, and exceptions take priority over length.
TAS is not a claim of full ASD-STE100 compliance.
The authoring method distinguishes context load from human cognitive load, discloses branch-only reference behind reliable pointers, and gives steps clear, exhaustive completion criteria.
Leading words anchor execution and invocation; positive instructions retain genuine safety guardrails.
Harness metadata such as `disable-model-invocation: true` requires verified consumer support, not an assumption from the source skill.

## Verify the package

Python 3.9 or newer, from the repository root:

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Checks cover required files, relative links, source checksums, loading contracts, relocation, and deliberate reference/method defects.
These offline checks validate the package, not live model behavior or measured token savings.

## Maintain and publish

This repository is the TAS authoring upstream. Maintain the standard here; consuming projects use its entrypoint and required references rather than maintaining normative copies.
Source updates are deliberate package maintenance, not automatic pulls from the Maker, Caveman, or writing-for-agents.
Update the standard, affected references, provenance, and checks together. Preserve upstream notices.
Only the root `SKILL.md` is a skill entrypoint; bundled style files use ordinary reference filenames.

Commit, remote publication, and live installation remain separate actions. A consuming project's pin names a committed revision, not unpublished working-tree changes.

## License

New TAS package material is [MIT-licensed](LICENSE).
The adapted TAS standard retains the [generic-devteam MIT notice](third_party/generic-devteam/LICENSE).
The writing-for-agents adaptation retains [Matt Pocock's MIT license](third_party/mattpocock/LICENSE).
Bundled Caveman material is covered by its [Apache-2.0 license](third_party/caveman/LICENSE), retained [MIT notice](third_party/caveman/LICENSE-MIT), [NOTICE](third_party/caveman/NOTICE), and [licensing explanation](third_party/caveman/LICENSING.md).
See [NOTICE.md](NOTICE.md) for attribution and exact scope.
