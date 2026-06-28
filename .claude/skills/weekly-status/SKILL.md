---
name: weekly-status
description: Draft a weekly status from the compounding update ledger. Use when the user types /weekly-status.
argument-hint: [--for <stakeholder-slug>]
---

# Weekly Status Skill

Use when the user types `/weekly-status`. Draft only; never sends.

## Behavior

1. Read the last 7 days of `me/updates/raw/YYYY-MM.md`. If the ledger is young or empty, fall back to
   recent `me/debriefs/` and project `## Notes`.
2. Read `me/weekly-goals.md` for the against-the-plan view.
3. Group the status into: **shipped / in-progress / risks-and-asks / narrative / against-the-plan**.
4. Default to one general status. `--for <slug>` tailors it to one person using their
   `## Concerns + Patterns` and the projects you share. Default coverage comes from
   `me/updates/config.md`.

## Rules

Operates on local files only; no connectors. Use the exec register from `me/communications.md`, lead
with the headline, concrete numbers where you have them, no em-dashes. Output is a draft for the owner
to review and send. Never sends.
