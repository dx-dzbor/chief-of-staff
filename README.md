# Personal OS

A file-based **chief-of-staff system** you run inside your AI coding agent. It is a curated set of
plain markdown files describing your role, projects, stakeholders, team, voice, and goals, plus a few
skills that turn that base into a morning brief, an end-of-day capture routine, a health audit, and a
weekly status draft.

No server. No database. No accounts. Just markdown and your agent.

## Why

Most of the context that makes you effective lives in your head or scattered across tools. A Personal
OS pulls it into one inspectable place, then compounds it: you write things down once during a daily
debrief, and the system reuses that capture in briefs and status updates. The result is less time spent
re-deriving context and more time on the work only you can do.

## 60-Second Quickstart

1. **Get the files.** Clone or download this repo, then open the folder in your AI agent (Claude Code
   or similar).
2. **Onboard.** Tell your agent:

   > Read `INIT.md` and set me up.

   It will interview you and fill in your `me/` files. Takes about 15 to 20 minutes.
3. **Use it daily.** Each morning run `/brief`. Each evening run `/debrief`. Weekly, run `/os-review`
   and `/weekly-status`.

Prefer to fill things in by hand? Open the `me/` files and the `_TEMPLATE.md` files and edit directly.
The `EXAMPLE-*.md` files show a fully filled, fictional version of each type. Delete them once you have
your own.

## What's In Here

```text
CLAUDE.md      bootloader: how your agent should read and use this workspace
CONTEXT.md     the architecture and data contract (the layers, the file schemas)
MANUAL.md      the guide: how to use each skill, the conventions, how to extend
INIT.md        the AI-led onboarding interview
me/            your knowledge base (identity, direction, projects, people, capture)
.claude/       the skills (brief, debrief, os-review, weekly-status) and command wrappers
```

Read `CONTEXT.md` for the design and `MANUAL.md` for day-to-day use.

## The Skills

| Command | What it does |
| --- | --- |
| `/brief` | Reads your base (and any connectors you have wired up) and writes a dated HTML brief: your current drive, today's focus, an acceleration check, calendar shape, where you are the blocker, who you are waiting on, project state, and stakeholder asks. Opens it in the browser. |
| `/debrief` | You paste a free-text dump of your day; it routes each line into the right project, stakeholder, and team files, and appends nuggets to the update ledger. Shows a plan and waits for approval before writing. |
| `/os-review` | A read-only audit: stale advice, inactive projects, dormant relationships, placeholder text left unfilled. |
| `/weekly-status` | Drafts a weekly status from the update ledger and your weekly goals. |

The `brief` and `debrief` skills carry the full operating logic but run with **zero dependencies**: the
agent authors the HTML brief itself, and every connector (Slack, Gmail, Calendar, meeting notes) is
optional and skipped gracefully when absent. Wire up connectors or drop in a script-based renderer
whenever you like, and tune the skills to fit how you work. See "Extending the System" in `MANUAL.md`.

## Conventions Worth Knowing

- Everything is dated and attributed.
- Skills draft and propose. They never auto-send anything.
- Audits are read-only.
- No em-dashes in drafted output.

## License

MIT. See `LICENSE`.
