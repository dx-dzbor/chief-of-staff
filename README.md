![Personal OS: AI Chief of Staff](docs/banner.png)

# Personal OS: AI Chief of Staff

A file-based chief of staff for people managing projects, decisions, and relationships. Your private context lives in plain markdown. A short onboarding flow and five daily skills turn it into a brief, captured notes, decision follow-through, a weekly status draft, and visual explanations. No server, database, or connector is required.

![How the Personal OS works](docs/diagram.svg)

## The loop

| When | Command | Result |
| --- | --- | --- |
| First use | `/onboard` | Three questions, a private working picture, and a first brief. |
| Morning | `/brief` | An HTML brief led by today's priority, decisions needed, and follow-ups. |
| Evening | `/debrief` | Your raw dump saved verbatim; clear routine facts filed; material or uncertain changes shown for review. |
| Weekly | `/os-review` | A read-only check for overdue decisions, stale commitments, and gaps in the base. |
| Weekly | `/weekly-status` | A concise draft based on update events, goals, and current decisions. |
| Anytime | `/eli5 <topic>` | A self-contained HTML explanation with a real diagram, plain words, and source boundaries. |

The loop compounds: capture an event once, then use it in the next brief and status. `me/decisions.md` keeps the current decision picture; the dated update ledger keeps the history.

## Get started

```bash
git clone https://github.com/dx-dzbor/chief-of-staff.git
cd chief-of-staff
```

Open the folder in Claude Code and run **`/onboard`**. In another agent, say **"Read `INIT.md` and onboard me."** The agent asks about your work, your most important near-term outcome, and your next move, one question at a time. It confirms a short working picture, creates your private `me/` files, and makes a first brief. It can learn projects, people, and voice examples later. Claude Code exposes the commands in `.claude/commands/`; other agents can read the corresponding `.claude/skills/*/SKILL.md` files.

After that first brief, onboarding offers to help set up an optional local weekday schedule. The command works without a schedule. Run `/debrief` after work and `/os-review` with `/weekly-status` each week. Try `/eli5 explain how a decision moves through this system` to see the visual format.

Open the [fictional ELI5 example](docs/eli5-example.html) locally to see the intended HTML page and diagram.

## What is in the repo

```text
CLAUDE.md          short operating contract and context loading rules
CONTEXT.md         file formats and write boundaries
MANUAL.md          daily loop and customization guide
INIT.md            guided onboarding
templates/me/      public starter files and fictional examples
me/                your private working context, ignored by Git after onboarding
.claude/skills/     onboard, brief, debrief, os-review, weekly-status, eli5
.claude/commands/   Claude Code command wrappers
scripts/           safe private-context bootstrap
docs/              diagram and fictional examples
```

`templates/me/` includes starter files, entity templates, and fictional `EXAMPLE-*.md` files. `/onboard` uses `scripts/bootstrap_me.py` to copy the starters into private `me/` without the examples or overwriting existing files. [The decision example](docs/decision-example.md) shows the active and closed record format.

## How it stays useful

- The default voice is plain, crisp, and actionable. Add your real writing samples to `me/communications.md` so drafts sound like you.
- Briefs show only real signal. Missing connectors do not block them and are not mistaken for an empty inbox.
- Debrief writes straightforward notes directly. It asks before changing decisions, obligations, entities, or uncertain facts.
- Skills draft and propose; they never send a message. `/os-review` never writes.
- Generated `briefs/` and `explainers/` HTML is ignored by Git because it may contain private context.
- The entire populated `me/` folder is ignored by Git. Review `git status` before pushing; never force-add private context to a public repository.

Read [the manual](MANUAL.md) to tune the skills or add optional Slack, email, calendar, and meeting-note connections. The core works from local markdown alone.

## License

MIT. See [LICENSE](LICENSE).
