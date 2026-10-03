# Personal OS context

This is a file-based chief-of-staff template. Plain markdown is the source of truth; skills turn it into priorities, capture, follow-through, status drafts, and visual explanations. It needs no server, database, or connector. Claude Code provides the slash-command wrappers; an agent that can read markdown skills can use the same instructions directly. `/onboard` copies public starter files from `templates/me/` into private, Git-ignored `me/`. Templates and fictional examples are never evidence about the owner.

## Operating loop

```text
current drive + goals + projects + people + decisions + waiting-on
                         ↓ /brief
                  today's actions (HTML)
                         ↓ do the work
                      /debrief
          raw dump + routine facts + reviewed changes
                         ↓
             decision follow-through + update ledger
                         ↓ /os-review and /weekly-status
                 clean-up actions + status draft
```

The base compounds because a fact is captured once and reused. Keep a current home for each state: project files for project state, people files for relationship context, `me/waiting-on.md` for current obligations owed by others, and `me/decisions.md` for current decisions. The update ledger is dated event history, not a second copy of current state.

## Files

- `CLAUDE.md`: short operating contract and context loading rules.
- `INIT.md`: short onboarding flow; `.claude/skills/onboard/SKILL.md` is its command entry point.
- `scripts/bootstrap_me.py`: copies public starters into private `me/` without overwriting and checks Git privacy.
- `templates/me/`: public starter files, entity templates, and fictional examples. Do not write the owner's context here.
- `me/onboarding.md`: private setup stage and resume point.
- `me/index.md`: orientation and an auto-generated directory of projects and people. Preserve all content outside its `AUTO-GENERATED` markers.
- `me/current-drive.md`, `me/weekly-goals.md`: the current priority and near-term outcomes.
- `me/communications.md`: default voice plus the owner's audience rules and worked examples.
- `me/projects/*.md`, `me/stakeholders/{top,other}/*.md`, `me/team/*.md`: durable project and people context. Ignore `_TEMPLATE.md` and `EXAMPLE-*.md` as live evidence.
- `me/debriefs/YYYY-MM-DD.md`: the owner's raw words, saved verbatim.
- `me/updates/raw/YYYY-MM.md`: material dated events used for status drafts.
- `me/decisions.md`: active and closed decisions with follow-through.
- `me/waiting-on.md`: open and cleared obligations owed by others.
- `briefs/` and `explainers/`: generated HTML, excluded from Git by default.
- `me/`: all populated context, excluded from Git by default. Do not force-add it to this public template.

## Project and people files

Project frontmatter uses `name`, `status` (`active | paused | done`), `coverage` (`full | selective | passive`), `aliases`, and `priority` (`P0` to `P3`). Optional connector selectors are `slack_channels`, `slack_people`, and `email_filters`; `stakeholders` links people to the project. The usual headings are Overview, Coverage Policy, Current State, Open Questions / Blockers, Plan / Next Steps, and Notes.

Stakeholder frontmatter uses `name`, `role`, `projects`, and `aliases`, with optional `slack_handle`. Its durable sections are Relationship Context, Concerns + Patterns, Advice & Suggestions, Open Asks, and Interaction Log. Team frontmatter uses `name`, `level`, `manager`, `joined`, `projects`, `aliases`, and `status`; its sections are Role & Work, Strengths & Archetype, Career Aspirations, Stakeholder Feedback, and Notes. See each `_TEMPLATE.md` for the exact shape.

Aliases help debrief route clear mentions. An alias match is evidence of a possible destination, not permission to invent a claim or update a record whose meaning is uncertain.

## Decisions and events

`me/decisions.md` has `## Active` and `## Closed`, newest first. A record has a stable daily ID (`D-YYYYMMDD-NN`), decision date, short decision, source, and `owner`, `next`, and `checkpoint` when they apply. Use `none` for unknown or inapplicable optional fields. Add a brief reason only when supported. A closed record keeps its original text and adds close date, outcome, and `closed-source`. The fictional format is in `docs/decision-example.md`.

The update ledger keeps one-line events: `- [type] (proj: <slug>; ppl: <slug>) <concrete event>`. Valid types are `shipped | progress | decision | win | risk | ask | narrative`. A decision event enters the ledger when the reviewed decision record is created or materially changed. Weekly status reads events for what happened and decisions for what remains open.

## Write boundaries

- `/brief` may write its HTML, the auto-generated index region, and a dated operating log line. It does not change knowledge records.
- `/debrief` saves the supplied raw dump and clear additive facts directly. It presents decisions, obligation changes, new entities, state rewrites, and uncertain routing for review before applying them. Skipping pending changes does not undo routine capture.
- `/os-review` reads only. `/weekly-status` drafts only. `/eli5` writes only its generated HTML.
- Skills never send email or messages on the owner's behalf.

Date and attribute captured facts. Append dated notes oldest first under `### YYYY-MM-DD`; keep current decision and waiting-on lists newest first. Turn relative dates into absolute dates when the source permits it. Follow `me/communications.md` for tone and avoid em dashes in drafted output.

## Optional signals

Slack, email, calendar, and meeting notes may enrich relevant work if connected. A missing connector is not an error or evidence of no activity. Keep source links and distinguish observed signals from recommendations. The core system must work from markdown alone.
