# Skill mechanics

Read this branch when the commissioned text is a skill.
It adapts Matt Pocock's required `SKILL-MECHANICS.md`; see [attribution](../NOTICE.md#writing-for-agents).
Use the [TAS standard](tas-authoring-standard.md) for the shared writing method.

## Invocation

Choose who must reach the skill before choosing metadata:
- **model-invoked:** The agent or another skill must discover and invoke it. Write a model-facing description with its distinct trigger branches. This discovery adds context load; user invocation can remain available too.
- **user-invoked:** Only the human needs to choose it. Prefer supported explicit-only discovery/invocation controls and a short human-facing summary. The human carries the cognitive load of remembering the skill.

Verify the current harness's metadata parser, catalog visibility, invocation controls, and reference-loading behaviour before relying on them.
A hidden description, blocked autonomous invocation, blocked cross-skill calls, and zero context load are separate claims.
Frontmatter alone does not establish any of them.

The original method uses `disable-model-invocation: true` to implement explicit-only invocation and remove the description from model context.
Apply that mechanism only where its semantics are verified in the consuming harness.
An unrecognized field may leave the description visible and the skill callable.
Report an unsupported control rather than claiming it enforces the design; use supported discovery controls or an explicit document entry instead.
Keep this a current capability check, not a permanent restriction on any harness.

A model-invoked reference skill can own shared material when all consumers can invoke it.
Place shared material in a plain reference when its consumers cannot invoke each other.
Give every consumer a reliable pointer and retain the shared reference as the single authority.

## Splitting by invocation

Split off a model-invoked skill when a distinct leading word needs independent reach in actual prompts, or another skill must invoke it.
Require that independent reach to justify the recurring description cost.
Use the standard's completion/context-boundary test for sequence splits instead of treating another file as a fresh context.

## Router

When many explicit-only skills exceed what the human can remember, consider one explicit entry listing their distinct uses.
Use it only when that index reduces a real human discovery burden and the harness supports the intended access.
In the original explicit-only design, the router hints at choices; the human invokes the destination.
Verify whether the actual harness permits cross-skill invocation before promising automatic dispatch.
