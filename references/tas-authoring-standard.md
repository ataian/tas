# TAS: Technical Agent Specification

**Scope:** All agent-context Markdown: SOULs, skills, references, setup/update recipes, and project instructions.
**Language:** English for development communication and artifacts, including role communication, tickets, handoffs, findings, and technical documentation. Preserve exact identifiers, quotations, error messages, and deliberately localized product text.
**Basis:** Original Caveman style plus the instruction contracts below; not full ASD-STE100 compliance.

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
- Use short statements and concrete bullets; omit whole-plan repetition and routine procedures.
- Keep decisions, accepted exceptions, consequential failures, blockers, outcomes, and verdicts on the existing card; omit routine command/log inventories and successful-test catalogues.

## Rewrite acceptance checks

Before acceptance, verify:
- Explicit owners for role, approval, security, and review invariants; effective conditions and exceptions.
- Correct Kanban tools and target roles.
- Model, reasoning, and Code-only boundaries remain effective through delegation.
Verify that references exist and load when needed, and runtime prerequisites remain available at execution time.
Rehearse ordinary and failure cases before deployment.
