# Personal OS Manual

This is the day-to-day guide. For the architecture and data contract, read `CONTEXT.md` first. For
setup, use `INIT.md`.

## 1. What You Have

A Personal OS is a knowledge base (`me/`) plus skills (`.claude/skills/`). You curate the base; the
skills read and write it. Everything is plain markdown, so you can edit any file by hand at any time,
and your AI agent can read all of it.

## 2. The Six Layers

| Layer | Files | Purpose |
| --- | --- | --- |
| Identity and voice | `profile`, `personal-narrative`, `communications`, `expectations`, `role`, `role-expectations` | Who you are, how you write, how you are judged. Keeps drafts sounding like you. |
| Direction | `current-drive`, `weekly-goals`, `long_term_goals`, `waiting-on`, `exec_steer` | Where you are pointed, this week and this year. |
| Project memory | `projects/*.md` | One durable file per active initiative. |
| People memory | `stakeholders/top|other/*.md`, `team/*.md` | Relationships, what people care about, what is owed. |
| Capture and output | `debriefs/*`, `updates/*` | Raw daily dumps and the compounding update ledger. |
| Signal layer | (optional) | Where live or mocked signals would feed in. Not included by default. |

## 3. The Daily / Weekly Loop

```text
morning   /brief           what matters today
day       (do the work)
evening   /debrief         capture the day, route it into the base
weekly    /os-review       health check
weekly+   /weekly-status   draft a status from the ledger
```

### `/brief` - the morning brief

Reads your base and produces a prioritized brief: your current drive, today's focus, where you are the
blocker, who you are waiting on, project state, stakeholder open asks, and a quick narrative and
expectations check. It does not write anything. Run it first thing.

The version shipped here outputs the brief in chat as markdown. It is intentionally simple. See
"Extending the System" if you want a richer rendered output.

### `/debrief` - the evening capture

You paste a free-text dump of your day. The skill matches each line against the `aliases` in your
project and people files and proposes a routing plan: which lines go to which project `## Notes`, which
stakeholder `## Interaction Log` or `## Advice & Suggestions`, which team `## Notes` or
`## Stakeholder Feedback`. It also extracts waiting-on items and ledger nuggets. It shows the plan and
waits for your approval before writing. This is the engine that makes the base compound, so debrief
even when the day was quiet.

### `/os-review` - the health audit

Read-only. Flags stale advice, projects that have gone quiet, stakeholders you have not logged in a
while, frontmatter problems, orphaned files, and leftover placeholder text. Run it weekly to keep the
base honest.

### `/weekly-status` - the status draft

Reads the last seven days of the update ledger (falling back to recent debriefs and project notes) and
your weekly goals, then drafts a status grouped into shipped / in-progress / risks-and-asks / narrative
/ against-the-plan. Draft only; you decide what to send.

## 4. The Compounding Update Engine

The point of `/debrief` is not just a diary. Each debrief appends terse nuggets to
`me/updates/raw/YYYY-MM.md`:

```text
- [shipped] (proj: aurora; ppl: riley) cut p95 latency 40% on the ranker path
- [risk] (proj: atlas; ppl: sam) staffing gap will slip the July date unless backfilled
```

`/weekly-status` reads those nuggets instead of re-reading your raw debriefs. Monthly and quarterly
roll-ups read the tier below, never the raw dumps. Cheap to capture, cheap to summarize, so it
compounds instead of becoming a chore. The valid `type` tags are
`shipped | progress | decision | win | risk | ask | narrative`.

## 5. File Schemas (Quick Reference)

See `CONTEXT.md` for the full schemas. The short version:

- **Project** (`me/projects/<slug>.md`): frontmatter with `name, status, coverage, slack_channels,
  slack_people, stakeholders, email_filters, aliases, priority`; headings Overview / Coverage Policy /
  Current State / Open Questions / Plan / Notes.
- **Stakeholder** (`me/stakeholders/top|other/<slug>.md`): frontmatter `name, slack_handle, role,
  projects, aliases`; headings Relationship Context / Concerns + Patterns / Advice & Suggestions /
  Open Asks / Interaction Log.
- **Team** (`me/team/<slug>.md`): frontmatter `name, level, manager, joined, projects, aliases,
  status`; headings Role & Work / Strengths & Archetype / Career Aspirations / Stakeholder Feedback /
  Notes.

Each folder has a `_TEMPLATE.md` (copy it for a new entry) and an `EXAMPLE-*.md` (a filled fictional
sample you can delete).

## 6. Conventions (Non-Negotiable)

- **Aliases drive routing.** Be generous with `aliases` so `/debrief` finds the right file.
- **One source of truth.** `index.md` reflects the files; do not duplicate lists.
- **Dated and attributed.** `YYYY-MM-DD | source | content`. Relative dates become absolute on write.
- **Append oldest-first** under `### YYYY-MM-DD` headings.
- **Drafts, not sends.** Skills propose; you send.
- **Read-only audits.** `/os-review` never writes.
- **No em-dashes** in drafted output.

## 7. Customizing

- **Tune `coverage` per project** (full / selective / passive) to control how much a brief surfaces.
- **Edit the skills.** They are plain markdown under `.claude/skills/`. Change the brief sections, add
  checks to the audit, or adjust the status grouping to fit how you work.
- **Add your own skills.** Drop a new `SKILL.md` under `.claude/skills/<name>/` and a wrapper under
  `.claude/commands/`. Good candidates: a stakeholder-update drafter, a decision stress-test, a
  generic activity briefing.

## 8. Extending the System

The shipped `/brief` and `/debrief` are deliberately basic so the repo runs anywhere with no
dependencies. Two common upgrades:

- **A richer brief.** Replace the prose brief with a script that gathers signals and renders a
  formatted (for example HTML) brief. Keep the same inputs (`current-drive`, `weekly-goals`,
  `projects/*`, `stakeholders/top/*`, `waiting-on`, `expectations`) and have the skill call your
  script. Point the `/brief` skill at it.
- **Live signals.** Add a signal layer that pulls from Slack, email, or calendar into a structured
  file, then have `/brief` read that alongside the markdown base. Keep the safe-by-default rule: read
  and draft, never auto-send.

Whatever you add, keep the invariants in section 6. They are what make the system trustworthy.
