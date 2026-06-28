---
name: os-review
description: Read-only health audit of the Personal OS base. Use when the user types /os-review or asks for an OS health check.
---

# OS Review Skill (read-only)

Use when the user types `/os-review`. This skill never writes files.

## Behavior

Audit the local base under `me/` and report findings only.

## Checks

1. **Stale advice:** stakeholder `## Advice & Suggestions` items still open more than 14 days.
2. **Inactive projects:** no mention in `me/log.md` or the project `## Notes` in 7 or 14 days.
3. **Dormant stakeholders:** empty or old `## Interaction Log`.
4. **Frontmatter inconsistencies:** missing required fields, slugs not matching filenames, broken or
   empty `aliases`.
5. **Orphaned files:** project or person files not referenced by any other file's frontmatter.
6. **Team-member staleness:** empty `## Career Aspirations` or `## Stakeholder Feedback`, or old
   `## Notes`.
7. **Unfinished setup:** leftover `[PLACEHOLDER]`, `[YOUR_`, `TODO`, or "to be filled" text, and any
   remaining `EXAMPLE-*.md` files.

## Output

A severity-tagged list grouped by check, ending with a short set of clean-up questions for the owner.
Never writes.
