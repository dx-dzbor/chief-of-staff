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
| Capture and output | `debriefs/*`, `updates/*`, `briefs/*.html` | Raw daily dumps, the compounding update ledger, and generated briefs. |
| Signal layer | (optional) | Slack, email, calendar, meeting notes. None bundled; the skills use them if present and skip them gracefully if not. |

## 3. The Daily / Weekly Loop

```text
morning   /brief           write briefs/YYYY-MM-DD.html, open it, refresh the index, log an entry
day       (do the work)
evening   /debrief         capture the day, route it into the base after approval
weekly    /os-review       health check
weekly+   /weekly-status   draft a status from the ledger
```

The loop has a deliberate asymmetry: `/brief` is a read pass that writes only the brief, the index, and
a log line; `/debrief` is the only write pass for real knowledge, and it always shows a plan first.

### `/brief` - the morning brief

Reads your base (and any connectors you have wired up) and writes a dated HTML brief to
`briefs/YYYY-MM-DD.html`, opens it, refreshes `index.md`, and appends a log entry. The HTML is the
artifact, so it does not summarize itself in chat. Sections, in order: driving end-to-end, today's
focus, an acceleration check (the signature "is this maximally accelerated?" lens), today's calendar
shape, where you are the blocker, who you are waiting on, project updates, top stakeholders, broader
context, and a Monday expectations check. Run it first thing.

No Python is required: the agent authors the HTML directly. If you want a faster, deterministic
renderer, you can drop in a script later, see "Extending the System."

### `/debrief` - the evening capture

You paste a free-text dump of your day (and the skill optionally enriches it from today's meeting
notes if you have a provider wired up). It matches each line against the `aliases` in your project and
people files and proposes a routing plan: which lines go to which project `## Notes`, which stakeholder
`## Interaction Log` or `## Advice & Suggestions`, which team `## Notes` or `## Stakeholder Feedback`.
It also opens and clears waiting-on items and appends ledger nuggets. It shows the full plan and waits
for your approval before writing anything, then saves your raw dump verbatim. This is the engine that
makes the base compound, so debrief even when the day was quiet.

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

The shipped `/brief` and `/debrief` carry the full operating logic but run with zero dependencies: the
agent authors the HTML brief itself and every connector scan is optional. Common upgrades:

- **A script-based brief renderer.** For speed and deterministic output, replace the agent-authored
  HTML with a script that gathers signals and renders the page. Keep the same inputs (`current-drive`,
  `weekly-goals`, `projects/*`, `stakeholders/top/*`, `waiting-on`, `expectations`) and the same
  section order so it is a drop-in, then point the `/brief` skill at it.
- **Live connectors.** Wire up Slack, Gmail, Calendar, or a meeting-notes provider. The skills already
  describe how each is used (`/brief` scans them; `/debrief` enriches the dump from meeting notes).
  Keep the safe-by-default rule: read and draft, never auto-send.

Whatever you add, keep the invariants in section 6. They are what make the system trustworthy.
