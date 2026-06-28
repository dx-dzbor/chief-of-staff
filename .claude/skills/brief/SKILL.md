---
name: brief
description: Generate the morning chief-of-staff brief. Use when the user types /brief, asks for a morning brief, today's context, or what's on their plate today.
argument-hint: "(optional) date override or focus area"
---

# /brief - Morning Brief

Read the `me/` base, scan any configured external signal, write a dated HTML brief, open it, refresh
the index, and append a log entry. The HTML is the artifact. Do not summarize it in chat.

> No Python is required: you author the HTML directly. A user can later swap in a script renderer; keep
> the same inputs and section order so it stays a drop-in replacement.

## Hard Rules

- Read `me/communications.md` first and obey its style rules in all rendered prose. No em-dashes.
- Read-only on knowledge: the only files you write are the HTML brief, the regenerated `me/index.md`,
  and the `me/log.md` entry.
- Every external scan is optional. If a connector is missing, note it internally and continue. Missing
  integrations never block the brief.
- Use today's system date unless the user passed a date override.

## Read (in order)

1. `me/index.md` (orientation), `me/profile.md`, `me/communications.md`.
2. `me/current-drive.md`, `me/expectations.md`, `me/weekly-goals.md`.
3. Last 3 entries of `me/log.md` (carryover and recent loop state).
4. All routable project files under `me/projects/**/*.md` (frontmatter has `aliases`; skip files
   without it, like `_TEMPLATE.md`). Honor each project's `coverage`.
5. All `me/stakeholders/top/*.md` and `me/stakeholders/other/*.md`, all `me/team/*.md`.
6. `me/waiting-on.md`, `me/calendar.md`.

## Optional external scans (use if available, else skip with a note)

- **Slack, last 24h.** Per project, pull its `slack_channels` and `slack_people`. Apply `coverage`:
  `full` surfaces meaningful signal and suggested actions; `selective` only stakeholder-authored or
  materially important items; `passive` stays quiet unless directly mentioned. Roll up top-stakeholder
  activity to one line (channels, count, topic) without re-listing project messages. Scan any broader
  context channel groups for stakeholder posts and large items only (incidents, launches, leadership).
- **Gmail, last 24h.** For projects with `email_filters`, surface subject, sender, snippet, link.
- **Calendar, today + tomorrow.** Otherwise fall back to `me/calendar.md`. Flag `prep needed` when an
  agenda/doc is attached, the title implies review/decision/1:1, or the meeting touches a project with
  open blockers or a stakeholder with open asks. Cross-reference attendees to stakeholder `## Open Asks`
  and stale `## Advice & Suggestions` and attach inline. Flag conflicts and early starts.
- **Where I am the blocker.** Resolve the user's identity, then surface unreplied Slack DMs/mentions,
  threads where the last reply is not the user's, and human email threads awaiting the user. Render each
  as one action line: `<who> - <what they need> - <link>`. Skip ambient chatter.

## HTML sections (in order; omit a section cleanly if it has nothing real)

1. **Driving end-to-end** - from `current-drive.md`: name, period, narrative one-liner, blocker, a
   one-line nudge for today. Renders first always; if no drive is set, show a banner: "No current drive
   set - pick one before end of day."
2. **Today's focus** - 3 to 5 bullets synthesized from carryover, weekly goals, top project state,
   calendar, and waiting-on. Current-drive items sort to the top. Lead with the single most important.
3. **Acceleration check** - the signature lens: "Is this maximally accelerated?" (replace with the
   user's own lens if they have one). For the drive and top 1 to 2 projects, give 2 to 3 concrete
   faster moves (a decision waiting on someone, a step that could be parallelized, an ask to make
   today). Omit the section entirely if there is no real signal; never use filler.
4. **Today's shape** - today's remaining events and tomorrow's, as one-liners. Lead with the next
   meeting needing prep and say what prep. Call out conflicts, stakeholder meetings with open asks.
5. **Where I am the blocker** - the blocker scan, action-framed. Omit if empty.
6. **Waiting on others** - from `waiting-on.md` `## Open`, newest first, overdue/stale flagged. Do not
   duplicate items already attached to a meeting above unless the chase is urgent.
7. **Project updates** - one subsection per active project: status, 24h signal, stakeholder messages
   inline, 2 to 4 suggested actions, matching email, blockers. Apply coverage.
8. **Top stakeholders** - roll up activity, surface open or stale advice and open asks. Preparation,
   not exhaustive activity.
9. **Broader context** - configured channel groups: stakeholder posts and materially large items only.
10. **Expectations check** - run on Mondays, or if absent from the last 7 log days. From
    `expectations.md` + last 7 log entries + activity: 4 to 6 bullets on which dimensions showed up,
    which went quiet, and evidence. Omit on other days unless a real signal warrants it.

This is an action surface, not an inbox digest. Name the people who did good work so credit is easy.

## Post-actions

1. Write the HTML to `briefs/YYYY-MM-DD.html` (visual, section headers, bullets, links to Slack
   permalinks and email threads where available).
2. Open it in the browser if the environment supports it.
3. Regenerate `me/index.md` from frontmatter, preserving its manual sections (see the AUTO-GENERATED
   markers in that file).
4. Append a brief entry to `me/log.md`:
   `## [YYYY-MM-DD HH:MM] brief` then one line with counts (projects scanned, messages, emails,
   calendar events, prep-needed, blocker items).
5. Return only one short line:
   `morning brief written to briefs/YYYY-MM-DD.html and opened in browser`
