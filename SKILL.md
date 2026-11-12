---
name: tas
description: TAS for authoring and reviewing agent instructions.
version: 1.1.0
author: Max, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tas, authoring, instructions, review]
    related_skills: []
---

# TAS: Technical Agent Specification

Write concise agent instructions that preserve authority, meaning, and verifiable outcomes.
This package contains its standard and style references. It needs no Maker, network service, or separate Caveman installation.

## When to Use

- The user requests TAS, including work outside the package's source project.
- Draft, revise, compress, or review agent-context Markdown: SOULs, skills, references, recipes, and project instructions.
- Propose agent-instruction wording before an authorized file edit.

## Prerequisites

Use a file-reading capability and access to the commissioned source text.
Resolve package paths relative to this `SKILL.md`, not the current working directory.
If a required file is missing or unreadable, report its path and stop the affected step.

## Procedure

1. Read [the TAS standard](references/tas-authoring-standard.md) completely on every invocation.
2. Read [the TAS Caveman reference](references/caveman.md) unless that bundled version is already available in context.
3. For review findings, also read [the TAS Caveman Review reference](references/caveman-review.md), including Auto-Clarity.
4. When the commissioned text is a skill, read [Skill mechanics](references/skill-mechanics.md) before choosing invocation, metadata, or a skill split.
5. Read the target's applicable instructions and current text. Identify the requested result, authorized scope, and existing approval gates.
6. Apply the TAS standard to the commissioned text. Preserve exact technical payload, conditions, exceptions, and required evidence.
7. Compare revised wording with its source. Account for every changed instruction and verify every applicable acceptance check in the TAS standard before claiming completion.
8. Report the result briefly. State unresolved decisions, missing checks, and concrete blockers explicitly.

## Boundaries

Use the bundled Caveman files as style references for the commissioned work.
TAS extends their style to persisted prose, preserving clarity and safety exceptions.
Retain the assigned review procedure, evidence checks, and native review outcomes; style guidance does not replace them.

This authoring standard grants no installation, file-edit, commit, publication, deployment, or infrastructure permission.
Other agents receive TAS only through instructions they actually load; package availability alone does not activate it for them.

## Verification

- Preserve actors, actions, inputs, triggers, conditions, approval owners, exceptions, and required results.
- Retain evidence requirements and distinguish planned, implemented, tested, reviewed, approved, published, and deployed states.
- Verify that moved instructions remain reachable through required references.
- Keep unrelated text and behavior outside the requested change.
- Use plain prose when compression would obscure meaning or a safety boundary.
