# TAS: Technical Agent Specification

**Scope:** All agent-context Markdown: SOULs, skills, references, setup/update recipes, and project instructions.
**Language:** English for development communication and artifacts, including role communication, tickets, handoffs, findings, and technical documentation. Preserve exact identifiers, quotations, error messages, and deliberately localized product text.
**Basis:** Matt Pocock's writing-for-agents method, TAS authority/evidence contracts, and Caveman style; not full ASD-STE100 compliance. See [attribution](../NOTICE.md).

## Purpose

Write concise instructions that preserve authority, meaning, and verifiable outcomes.

## Style source

Read the TAS-adapted `caveman` from [the bundled reference](caveman.md) unless already available; authoring does not authorize installation.
Apply its style to persisted prose too, overriding its persisted-content exception.
Use the TAS-adapted [`caveman-review`](caveman-review.md) with Auto-Clarity for findings; retain the assigned review procedure and native outcomes.
Preserve technical payload verbatim and retain safety warnings, conditions, and exceptions. Clarity wins over length limits.
Other roles receive these scope rules only through explicitly loaded instructions; this reference is not automatically loaded for them.

## Instruction contracts

1. Name the actor, action, input, and required result. Put triggers and conditions beside the action, and non-negotiable boundaries before procedures.
2. Preserve permissions, exceptions, and approval gates. Name the owner of unresolved decisions and their authorized escalation target.
3. Require observable evidence and verify required coverage before success claims. Report successes briefly, failures and missing checks explicitly.
4. Distinguish `planned`, `implemented`, `tested`, `reviewed`, `approved`, `published`, and `deployed`. Keep commits, publication, and deployment separately authorized.
5. Ground requirements, facts, permissions, tool capabilities, and test results in actual sources. Memory cannot override current implementation or accepted requirements.

## Content placement

- **SOUL:** Durable role, authority, prohibitions, invariants, escalation owner, workflow decisions, and communication.
- **Shared policy:** Common source-of-truth, Git safety, memory, and cost rules; only when reliably loaded by every consumer.
- **Skills/references:** Tool recipes, decision trees, tests, recovery, and examples.
- **Project context:** Repository paths, architecture, accepted requirements, deployment target, and setup records.
- **Runtime configuration:** Models/providers, reasoning limits, homes, environment bindings, and integrations. SOULs may require validation without duplicating volatile values.

## Context pointers

A context pointer names material outside the current context and states when to read it.
Skill descriptions and required-reference instructions are pointers; their wording determines whether the target is reached.
Front-load the leading word, state what the target contains, and give one trigger per distinct branch.
Collapse synonyms for the same branch and remove identity already supplied by the body.
Use a concrete path resolved against the referring file, or an equally unambiguous source binding.
Require the read when the branch fires; a link alone does not establish reliable loading.
Sharpen a weak pointer before inlining must-have material; inline it if the sharpened pointer still fails.
If a required target is missing or unreadable, report the exact target and stop the affected step.

## The two loads

**Context load** is the agent's recurring cost for always-loaded instructions and pointers, whether they fire or not.
**Cognitive load** is the human's cost of remembering which documents exist and when to invoke them.
Spend cognitive load where human judgement matters; remove it where it does not.
Disclosed material saves its own recurring context load but still pays for the pointer.
Material without a pointer depends entirely on the human's index.
Choose discoverability deliberately rather than treating either load as automatically wasteful.

## Information hierarchy

Separate ordered actions from reference material, then place each piece at the needed tier:
1. **In-file steps:** The primary ordered actions and their completion criteria.
2. **In-file reference:** Definitions, rules, and facts needed on demand; a flat peer-set of review rules can belong here.
3. **Disclosed reference:** Branch-specific material in another file, reached through an explicit context pointer.

Inline what every branch needs; disclose what only some branches need.
Use progressive disclosure to protect the hierarchy, not merely to shorten the entrypoint.
Keep the steps visible rather than burying them under branch-only reference.
Co-locate each concept's definition, rules, and caveats under one heading.
Treat scattering one meaning across headings separately from duplicating it.
Sprawl can persist even when every line is live and unique; disclose by branch or justified sequence boundary.

## Steps and completion

End each step with a completion criterion that is both checkable and exhaustive.
Name the observable boundary: the agent must distinguish done from not-done.
Set the demand explicitly: "every modified file accounted for" requires more legwork than "produce a change list".
Apply the same exhaustiveness bar to flat reference, such as "every applicable rule checked".
Sharpen the criterion first when later steps pull attention toward being done.
Split a sequence only when the bound remains irreducibly fuzzy and actual runs observe premature completion.
Hide later steps across a real context boundary, such as a handoff or subagent dispatch.
An inline call or second file alone leaves later steps in context and does not create that boundary.
Preserve required handoff information, authority, and evidence when splitting; each path carries what it needs.

## Leading words and positive prompting

Use leading words as established semantic anchors: compact concepts the model can already reason with, such as root cause, regression test, or tight loop.
Prefer an established concept over an invented label; define a new label when its meaning is genuinely needed.
In the body, the anchor guides execution; in a pointer, shared prompt/document/code vocabulary guides invocation.
Repeat the anchor rather than its full explanation, and retire restatements it replaces.
Preserve precise conditions and safety boundaries that the anchor alone cannot carry.
Prompt the positive target directly so attention lands on the intended action.
Retain genuine hard guardrails when a positive formulation cannot express the boundary, and pair them with the permitted action.
Authority, safety, approval, and evidence contracts remain binding.

## Pruning

Keep each meaning in a single source of truth; change its behaviour there and point consumers to it.
Treat the environment as a source of truth too: scripts, configuration, layout, and command help expose current facts.
Cache reasons, conventions, and gotchas that lookup cannot reveal, or facts whose lookup is genuinely expensive.
Leave cheap one-file or one-command lookups in their owning source instead of maintaining volatile copies.
Check every line for task relevance and current validity; disclose branch-only detail and remove stale sediment.
Evaluate no-ops against model-relative defaults, not the author's intuition.
Use actual runs to settle disputed behavioural effects; delete a proven no-op sentence rather than trimming it.
Test a weak leading word against the intended behaviour; choose a stronger established anchor when the weak one changes nothing.
Keep measured outcomes separate from plausible mechanisms, static wording checks, and model self-assessment.

## Compression contract

Classify each original instruction:
- `KEEP` role and safety invariants with their scope and conditions.
- `MOVE` details only to reliably loaded destinations.
- `MERGE` duplicates into one authoritative rule.
- `REMOVE` filler, redundant examples, or proven obsolete information.
- `REVIEW` ambiguity and conflicts rather than silently changing behavior.
Preserve approval gates and handled state transitions. Add no behavior merely to make a document appear complete.

## Rule pattern

**WHEN [trigger], [actor] MUST [action] using [source/tool]; THEN verify [result].**

Example: After `kanban_request_review`, verify the task status and reviewer assignment.

## Output contract

- Use concrete paths, commits, tests, and states when needed. Give reviewers reproducible findings and coders testable acceptance criteria.
- Bind tickets to the exact accepted plan, phase, and commits. Include concise story criteria and necessary technical context; keep excerpts aligned with that authoritative scope.
- For ticket bodies, use short statements and concrete bullets; omit whole-plan repetition and routine procedures.
- Keep decisions, accepted exceptions, consequential failures, blockers, outcomes, and verdicts on the existing card; omit routine command/log inventories and successful-test catalogues.

## Rewrite acceptance checks

Before acceptance, verify:
- Explicit owners for role, approval, security, and review invariants; effective conditions and exceptions.
- Correct Kanban tools and target roles.
- Model, reasoning, and Code-only boundaries remain effective through delegation.
- Every applicable step/reference has clear, exhaustive demand; every required pointer has a distinct trigger and reachable target.
Verify that references exist and load when needed, and runtime prerequisites remain available at execution time.
Rehearse ordinary and failure cases before deployment.

When evaluating a proposed upstream method, read its complete original guidance and required companions before comparison.
Compare the method as a whole: existing coverage, useful additions, and concrete conflicts.
Follow a user-selected baseline closely; justify deviations with actual runtime differences, authority/safety conflicts, or observed failures.
Verify harness mechanics against current documentation and their actual consumers; source inspection alone does not prove executed behaviour.
Use comparable runs when a behavioural claim needs evidence; authoring alone does not authorize benchmarks or deployment.
