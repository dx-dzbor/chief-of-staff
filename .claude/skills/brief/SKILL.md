---
name: brief
description: Generate a prioritized morning chief-of-staff brief from the Personal OS base. Use when the user types /brief or asks for a morning summary.
---

# Brief Skill

Use this skill when the user types `/brief` or asks for a morning summary.

> This is a basic, dependency-free version that reads the markdown base and writes the brief in chat.
> You can replace it with a richer renderer later; see "Extending the System" in `MANUAL.md`.

## Purpose

Prepare the owner for the day by reading the durable base under `me/` and surfacing what matters most
right now. Read-only: this skill does not write files.

## Inputs To Read

- `me/current-drive.md` for the one thing being driven end to end (the banner).
- `me/weekly-goals.md` and `me/log.md` for this week's outcomes and recent activity.
- `me/calendar.md` for fixed points coming up.
- `me/projects/*.md` for project state and `coverage` policy (respect it: surface less for selective
  or passive projects).
- `me/stakeholders/top/*.md` for `## Open Asks` (attach to relevant calendar items and roll up).
- `me/waiting-on.md` for things others owe you, with age and staleness.
- `me/expectations.md` for the expectations check.
- `me/personal-narrative.md` and `me/communications.md` for narrative framing and voice.

Skip any file that is missing or still full of placeholders, and say so briefly rather than failing.

## Output

Write the brief in chat as markdown, in this order. Omit a section if it has nothing real.

1. **Driving** - a one-line banner for the current drive: where it stands, the live blocker, the next
   move.
2. **Today's focus** - the three to five things that matter most today, pulled from weekly goals,
   overdue waiting-on items, and stakeholder open asks. Each with a one-line why.
3. **Calendar prep** - upcoming fixed points, with any stakeholder open asks attached inline.
4. **Where I'm the blocker** - anyone waiting on the owner.
5. **Waiting on others** - with overdue or stale flags.
6. **Project updates** - per active project, the latest state and any flag, weighted by `coverage`.
7. **Stakeholder roll-up** - top stakeholders with open asks or relationship moves to make.
8. **Narrative and expectations check** - one or two narrative plays, and a quick read on the
   expectation pillars (on-track / watch / gap).

## Rules

- Read-only. Do not write files.
- Lead with the driving banner and the most urgent focus items. Be specific and concise.
- Name the people who did good work; the brief should make it easy to give credit.
- No em-dashes.
- This base has no live connectors. Work only from the markdown files; do not invent signals.
