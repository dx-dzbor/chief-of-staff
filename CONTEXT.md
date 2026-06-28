# Personal OS Context

This repository is a **Personal OS**: a file-based chief-of-staff system that helps a busy
professional stay oriented across projects, stakeholders, team dynamics, and daily signals. It runs on
plain markdown plus a small set of skills, inside any AI coding agent (Claude Code, etc.). Nothing here
depends on a server, a database, or live connectors. You own the files; the skills turn them into
briefs, updates, and prep.

## The Core Idea

A Personal OS is two things working together:

1. A curated knowledge base of plain markdown files that hold what matters about the work: role,
   projects, relationships, voice, the narrative being pushed, and how the person is evaluated.
2. A small set of skills (slash commands) that read from and write back to that base. The user curates
   and directs; the skills turn the base into briefs, updates, and prep.

Three properties make it work:

- **One source of truth per thing.** The index reflects the files; lists are not hand-maintained in
  two places.
- **Compounding capture.** Daily debriefs feed weekly and monthly synthesis, so writing things down
  once pays off repeatedly.
- **Safe by default.** Skills draft and propose. Audits are read-only. Nothing is auto-sent.

## The Layers

1. **Identity and voice:** `me/profile.md`, `me/personal-narrative.md`, `me/communications.md`,
   `me/expectations.md`, `me/role.md`, `me/role-expectations.md`.
2. **Direction:** `me/current-drive.md` (the one thing driven end to end), `me/weekly-goals.md`,
   `me/long_term_goals.md`, `me/waiting-on.md`, `me/exec_steer.md`.
3. **Project memory:** `me/projects/*.md`, one durable file per active initiative.
4. **People memory:** `me/stakeholders/top|other/*.md` and `me/team/*.md`.
5. **Capture and output:** `me/debriefs/*`, `me/updates/*`, and the generated `briefs/*.html`.
6. **Signal layer (optional):** Slack, email, calendar, and meeting notes. The template bundles no
   connectors, but the skills use them if your environment has them and skip them gracefully if not. A
   markdown-only base still produces a full brief. See "Extending the System" in `MANUAL.md`.

## The Daily / Weekly Loop

```text
morning   /brief              read pass: write briefs/YYYY-MM-DD.html, refresh the index, log an entry
day       (do the work)
evening   /debrief            write pass: route the day into the base after approval, feed the ledger
weekly    /os-review          health check: stale advice, inactive projects, dropped balls
weekly+   /weekly-status      turn captured work into a status draft
```

The asymmetry is the safety model. `/brief` is a read pass: it reads the base (and any connectors) and
writes only the generated HTML, the regenerated index, and a log entry. `/debrief` is the only command
that writes meaningful new knowledge, and it never writes before showing a routing plan and getting
approval.

## Folder Contract

```text
personal_os/
  CLAUDE.md                      bootloader and reading order
  CONTEXT.md                     this architecture guide
  MANUAL.md                      how to use and customize the system
  README.md                      quickstart
  INIT.md                        AI-led onboarding interview
  me/
    index.md                     dashboard
    log.md                       append-only operating log
    profile.md  personal-narrative.md  communications.md  expectations.md
    role.md  role-expectations.md  current-drive.md  weekly-goals.md  waiting-on.md
    exec_steer.md  long_term_goals.md  calendar.md
    projects/                    one file per active initiative (_TEMPLATE.md + your files)
    stakeholders/top|other/      one file per stakeholder
    team/                        one file per team member
    debriefs/                    raw evening dumps
    updates/                     config.md, raw/YYYY-MM.md (ledger), YYYY-MM/_month-summary.md
  briefs/                        generated morning briefs (YYYY-MM-DD.html), git-ignored
  .claude/
    commands/                    slash-command wrappers
    skills/                      brief, debrief, os-review, weekly-status
```

## File Schemas

### Project file (`me/projects/<slug>.md`)

```yaml
---
name: Project Aurora
status: active            # active | paused | done
coverage: full            # full | selective | passive
slack_channels: [aurora-eng]
slack_people: [riley]
stakeholders: [sam]
email_filters:
  - subject_contains: "[Aurora]"
aliases: [aurora, project aurora]
priority: P0              # P0 | P1 | P2 | P3
---
```

Headings: `## Overview`, `## Coverage Policy`, `## Current State`, `## Open Questions / Blockers`,
`## Plan / Next Steps`, `## Notes`. `coverage` controls how much chatter a brief surfaces: full tracks
at detail level, selective only big or stakeholder-authored items, passive stays quiet.

### Stakeholder file (`me/stakeholders/top/<slug>.md`)

```yaml
---
name: Sam
slack_handle: sam
role: VP Engineering
projects: [aurora, atlas]
aliases: [sam]
---
```

Headings: `## Relationship Context`, `## Concerns + Patterns`, `## Advice & Suggestions` (dated, with
status), `## Open Asks` (surfaced against calendar items in the brief), `## Interaction Log` (dated,
oldest-first).

### Team file (`me/team/<slug>.md`)

```yaml
---
name: Riley
level: Senior Engineer
manager: [your_slug]
joined: 2025-03-01
projects: [aurora]
aliases: [riley]
status: active           # active | on-leave | departed
---
```

Headings: `## Role & Work`, `## Strengths & Archetype`, `## Career Aspirations`,
`## Stakeholder Feedback` (what others say, dated), `## Notes` (dated, oldest-first).

## The Compounding Update Engine

Event sourcing for status updates: capture cheap daily nuggets, then let each higher tier read the
tier below instead of reprocessing raw dumps.

```text
/debrief          appends nuggets to me/updates/raw/YYYY-MM.md          (write-ahead log)
/weekly-status    reads the last 7 days of that ledger                  (light view)
(monthly)         roll the month into me/updates/YYYY-MM/_month-summary (materialized view)
(quarterly)       roll up the monthly summaries                         (never re-reads raw)
```

Nugget format: `- [type] (proj: <slug>; ppl: <slug>) <one concrete line, numbers where possible>`
where `type` is one of `shipped | progress | decision | win | risk | ask | narrative`. The contract:
daily capture stays cheap, and higher tiers read summaries, not raw debriefs. That is what makes it
compound instead of becoming a chore.

## Conventions and Invariants

- **Aliases drive routing.** Every project and person lists `aliases`; `/debrief` matches dump text
  against them to decide which file a line belongs in.
- **One source of truth.** `index.md` reflects frontmatter; do not maintain the same list twice.
- **Dated and attributed.** Advice, asks, logs: `YYYY-MM-DD | source | content`. Relative dates become
  absolute on write.
- **Append oldest-first** under `### YYYY-MM-DD` headings in interaction logs and notes.
- **Drafts, not sends.** Update skills write files; they never post to Slack or email.
- **Read-only audits.** `/os-review` never writes.
- **No em-dashes** in any drafted output.

## What This Template Deliberately Excludes

No bundled connectors, database, persistent vector memory, auth, or multi-user permissions. The skills
will use Slack, Gmail, Calendar, or a meeting-notes provider if your environment exposes them, but
nothing is shipped or required, and every scan degrades gracefully. The base is plain markdown for you
and your agent to read and for the skills to operate on. The value here is the operating logic and the
data contract. See `MANUAL.md` for how to wire in connectors or swap the brief for a script renderer.
