# Personal OS manual

Run `/onboard` to set up the template; `INIT.md` contains the same flow for other agents. `CONTEXT.md` defines the file formats and write boundaries. This guide explains the daily loop.

## First session

The public starter files live in `templates/me/`. Onboarding runs `scripts/bootstrap_me.py` to copy them into a private `me/` folder, excluding fictional examples and preserving existing files. It asks about the owner's work, one near-term outcome, and the next concrete move, one question at a time. A rough dump can answer several questions at once. The agent shows its short operating picture before writing it, then makes a first `/brief`. `me/onboarding.md` records where to resume if the owner stops midway. See the [fictional conversation](docs/onboarding-example.md).

The first brief is useful with one project or even just one clear outcome. Add people, longer-term goals, voice samples, and status audiences when a real task needs them. Public templates are never evidence of the owner's work.

At the end, onboarding offers a recurring task. The owner can keep running `/brief` manually. If they opt into a weekday schedule, give the task a local working folder, time, and timezone. In Claude Desktop's Code tab, choose **Routines → New routine → Local**, point it to this folder, select weekdays, and use: "In this folder, run `/brief` for today. Use local `me/` context, save the HTML brief, and report the top action and link. Do not send messages." Run it once to check the output and permissions. Local tasks need the Desktop app open and the computer awake. A cloud routine clones the public repository and cannot read this machine's ignored `me/` files, so it is not the default for this template. [Claude Desktop scheduling guide](https://code.claude.com/docs/en/desktop-scheduled-tasks).

## Daily loop

**Morning: `/brief`.** The agent reads the current drive, goals, active decisions, waiting-on items, and relevant project and people context. It writes `briefs/YYYY-MM-DD.html`. The page starts with today's priority, decisions needed, and follow-ups. Calendar, project, stakeholder, and acceleration detail appears only when useful. The chat reply names the top action and links the page.

**Evening: `/debrief`.** Paste rough notes or voice transcription. The original text goes verbatim into `me/debriefs/YYYY-MM-DD.md`. Clear factual notes and update nuggets go to existing files directly. The agent shows a precise proposal before it records a decision, changes a commitment, rewrites current state, creates an entity, or applies uncertain routing. It reports what was saved and what remains pending.

**Weekly: `/os-review` and `/weekly-status`.** The audit is read-only and leads with overdue decision checkpoints, stale commitments, and other actionable gaps. The status command drafts from the last seven days of update events, weekly goals, and the current decision record. Use `/weekly-status --for <stakeholder-slug>` for a specific audience. You decide whether to send any draft.

**When explaining: `/eli5 <topic>`.** The agent creates `explainers/YYYY-MM-DD-<slug>.html`, a self-contained visual page with an inline SVG diagram, plain-language walkthrough, analogy and its limit, and sources when needed. It works for a general concept or a file in this workspace. Generated pages are private local artifacts by default and are ignored by Git.

## What gets written without review

An unambiguous note such as "Riley finished the pilot checklist" can enter an existing project and team history and the update ledger. The agent preserves who said it and when. The raw dump is always retained.

A statement such as "We might launch next week" is not a decision. A statement such as "We decided to pilot with one team" is a decision candidate; the proposed `me/decisions.md` entry is shown before writing. Opening or clearing a waiting-on item also waits for review because it changes the commitment picture. If the agent cannot tell which Sam or which project a line means, it leaves that line in the raw dump and asks for the routing it needs. A skipped proposal leaves already saved routine facts intact.

If you want to preview a debrief without changing files, ask for a **dry run** or **no write**.

## Decision follow-through

`me/decisions.md` is the current list. An active record has a stable ID, decision date, source, and any owner, next action, or checkpoint that applies. Closing a record preserves the decision and adds the outcome. See the [fictional example](docs/decision-example.md). The brief raises checkpoints and the audit flags overdue ones. The ledger's `[decision]` nugget records the event for weekly reporting; it does not replace the current record.

`me/waiting-on.md` is separate: it tracks what another person owes you, whether or not that item follows from a decision. Project files still hold the project's latest state. This separation lets the agent find the current answer without rereading every debrief.

## Voice and trust

The baseline voice is short, direct, and actionable. Lead with the point; say what happened, why it matters, and who does what next. Keep enough context to be clear on the first read. The owner can add audience rules and real examples to `me/communications.md` later. Facts and recommendations stay distinct, and missing evidence is named. No skill auto-sends a message.

## Customize and extend

Edit the markdown skills under `.claude/skills/` and their wrappers under `.claude/commands/`. Change the brief's focus or project `coverage` to fit your role. Add aliases to project and people files so debrief routing improves. Keep the decision and update formats stable so older notes remain readable.

Connectors are optional. When available, `/brief` can use Slack, email, calendar, and meeting notes as signals; `/debrief` can propose meeting-note candidates for review. A markdown-only base still produces a useful brief. If you replace agent-authored HTML with a renderer, keep the same input files and output paths so the commands remain compatible.

Generated HTML may contain sensitive personal or company context. `me/`, `briefs/`, and `explainers/` are ignored by Git; review a page before sharing it. The public repository contains only templates and fictional examples.

### Existing installs with tracked `me/` files

Older versions tracked starter files under `me/`. If you have filled those files, **copy the whole `me/` folder outside the repository before updating**. After updating, put your copy back in `me/` if needed and check `git check-ignore -v me/index.md` and `git ls-files me`: the first should show the `/me/` rule and the second should print nothing. A fresh clone of the updated template followed by copying your old `me/` folder into it is the simplest migration. Do not force-add `me/` to a public repository. If a previous commit already contains personal information, ignoring it now does not erase that history; review the repository's history and visibility separately.

After changing a skill, use the [fictional skill scenarios](docs/skill-scenarios.md) in a disposable copy to check both the output and what files changed.
