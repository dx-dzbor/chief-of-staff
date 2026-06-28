---
name: debrief
description: Capture an end-of-day dump and route it into the base. Use when the user types /debrief, wants to log the day, do an evening dump, capture today, or wrap up.
argument-hint: "(optional) inline text to debrief without prompting"
---

# /debrief - Evening Debrief

Capture the user's free-form end-of-day notes, optionally enrich with today's meeting notes, parse
against the routing map, show a routing plan, wait for approval, then append approved entries to the
base. This is the only skill that writes meaningful new knowledge.

## Hard Rules

- **Never write knowledge before the user approves the routing plan.** If they cancel, write nothing.
- Append to history; do not overwrite dated notes. Save the raw dump verbatim.
- Meeting-note enrichment is optional and degrades gracefully.
- No em-dashes. Use today's system date.

## Step 1 - Get the dump

If arguments are non-empty, treat them as the dump. Otherwise respond exactly:

```text
Okay, give me the debrief of your day. I will route it into the right projects, stakeholders, team
notes, advice, waiting-on, and the update ledger, and show you the plan before writing anything.
```

Then wait. Accept a multi-paragraph blob; voice-to-text is fine. Do not polish the saved raw dump.

## Step 2 - Load the routing map

Read `me/index.md`. Recursively load every `me/projects/**/*.md` whose frontmatter has `aliases` (skip
files without it). Load every `me/stakeholders/{top,other}/*.md` and `me/team/*.md`. Collect name,
slug, aliases, projects, and (for projects) channels, coverage, email filters. Team members match like
stakeholders but route to `## Notes`, not `## Interaction Log`.

## Step 3 - Pull today's meeting notes (optional)

If a meeting-notes provider is configured, list today's meetings and fetch title, attendees, summary,
decisions, action items. Convert useful items into routing candidates tagged
`meeting-notes: <title>`. If none or the tool fails, note it internally and continue with the dump only.

## Step 4 - Parse and classify

Walk the dump and any meeting-note candidates. One sentence may route to several places.

- **Project alias** -> that project's `## Notes`.
- **Stakeholder alias** -> that stakeholder's `## Interaction Log`.
- **Team member alias** -> that team member's `## Notes`.
- **Team member + a source giving feedback about them** -> team member's `## Stakeholder Feedback`
  (`- YYYY-MM-DD | <source-slug> | "quote or tight paraphrase"`).
- **Advice from a stakeholder** (keywords: advised, suggested, recommended, told me to, pushed me to,
  asked me to consider, feedback was) -> the interaction goes to `## Interaction Log` AND the advice to
  `## Advice & Suggestions` with status `new`.
- **Waiting-on** (waiting on/for, owes me, will get back to me, still need X from, chasing, blocked on
  <person>, <person> to send/decide) -> `waiting-on.md` `## Open`. If no known person matches, use
  `<unknown-person>` and flag it in the plan.
- **Waiting-on resolution** (got X back, heard from <person>, <person> sent/decided, unblocked by) ->
  propose `CLEAR` against an open item. Match person first, then topic; if several could match, list
  them and ask which. Never clear silently.
- **Update nugget** (material: shipped/progress/decision/win/risk/ask/narrative) -> `updates/raw/`.
  A line can yield both a routed note and a nugget. Keep nuggets concrete, with numbers/dates.
- **No alias match** -> `UNMATCHED`.

Match aliases case-insensitively on word boundaries; prefer the longest/exact match; route to multiple
entities only when the sentence genuinely references them.

## Step 5 - Show routing plan and wait for approval

Present every item with an origin tag, `(dump)` or `(meeting-notes: <title>)`, grouped by destination:
project notes, stakeholder logs, advice, team notes, team feedback, waiting-on OPEN, waiting-on CLEAR,
update nuggets, and UNMATCHED. For each unmatched item offer: archive only, route to an existing entity,
or create a new project/stakeholder/team file (if so, collect minimal frontmatter on approval).

Offer `Approve`, `Edit routing`, or `Cancel`. On Edit: apply corrections, show the revised plan, ask
again. On Cancel: write nothing and exit with one line.

## Step 6 - Write approved routes (only after approval)

- Project / stakeholder / team notes: append under the section and a `### YYYY-MM-DD` heading
  (create the heading if absent), oldest-first.
- Advice: prepend under `## Advice & Suggestions`, newest first, status starting at `new`, in the form
  `- **DATE** | STATUS | "verbatim or tightly preserved advice"` (status values: new, accepted,
  rejected, done, stale).
- Team feedback: prepend under `## Stakeholder Feedback`.
- Waiting-on OPEN: prepend to `## Open`:
  `- [ ] YYYY-MM-DD | <person-slug> | <what is owed> | needed-by: YYYY-MM-DD|none | re: [[<project-slug>]]`.
- Waiting-on CLEAR: move the matched item from `## Open` to `## Cleared`, preserving its text and adding
  `| cleared: YYYY-MM-DD | source: <dump|meeting-notes>`.
- Update nuggets: append to `me/updates/raw/YYYY-MM.md` under a `### YYYY-MM-DD` heading (create file
  and heading if absent): `- [type] (proj: <slug>; ppl: <slug>) <one concrete line>`.
- Promoted unmatched items: create the new file from the matching `_TEMPLATE.md` with minimal
  frontmatter and empty standard sections.

## Step 7 - Save the full debrief

Write the original dump verbatim to `me/debriefs/YYYY-MM-DD.md`. If the file exists, append under a
`## HH:MM` heading; do not overwrite. If meeting notes were used, append a `## Meeting notes` section
listing title, attendees, and a one-line summary.

## Step 8 - Refresh index and log

Regenerate `me/index.md` from frontmatter, preserving manual sections (AUTO-GENERATED markers). Append
to `me/log.md`:

```text
## [YYYY-MM-DD HH:MM] debrief
Processed evening dump (+G meeting-note meetings). Updated: <project-slugs> (N notes), <stakeholder-slugs> (M log, K advice). Waiting-on: +W open / C cleared. Nuggets: +U.
Carryover: <one line only if explicitly pending for tomorrow>
```

## Step 9 - Summary

Return one short line, for example:

```text
debrief routed: 2 projects, 3 stakeholders, 1 advice, 1 waiting-on, 3 nuggets. full text in debriefs/YYYY-MM-DD.md
```

Do not summarize the user's day in chat.
