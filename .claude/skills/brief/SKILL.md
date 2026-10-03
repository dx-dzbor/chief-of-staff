---
name: brief
description: Create an actionable morning chief-of-staff brief when the owner asks what matters today, requests a morning brief, or invokes /brief.
argument-hint: "(optional) date or focus area"
---

# Morning brief

Turn the owner's current context into a short decision and action surface. Write a self-contained `briefs/YYYY-MM-DD.html`, open it when possible, and return one line in chat with the top action and a link. Use the system date unless the user supplies another date.

## Gather the signal

If `me/` does not exist, make a sparse brief with one honest setup action: run `/onboard`. Do not use `templates/me/` or its examples as live context, and do not create `me/` as a side effect of `/brief`. Otherwise continue below.

Read `me/communications.md`, `me/current-drive.md`, `me/weekly-goals.md`, `me/decisions.md`, and `me/waiting-on.md`. Use `me/index.md` to find relevant active projects and people. If its generated lists are empty or stale, scan project and people frontmatter and refresh those lists. Open detail files when they affect today's priorities, meetings, or blockers; scan more widely only when the request requires it. Check recent `me/log.md` entries for carryover. Skip `_TEMPLATE.md`, `EXAMPLE-*.md`, and unfilled placeholder content as evidence.

If available, use relevant Slack, email, calendar, or meeting-note signals. Honor project `coverage`: `full` follows meaningful detail, `selective` surfaces material or stakeholder-authored items, and `passive` stays quiet unless directly relevant. Missing connectors never block a brief. Do not treat silence from an unavailable connector as evidence that nothing happened. Link to external items used.

## Decide what to show

Lead the page with:

1. **Today's priority:** the highest-leverage concrete move, grounded in the current drive and weekly goals. Name its owner and timing when known.
2. **Decisions needed:** active decisions at a checkpoint, overdue decisions, and decisions the owner must make today. Do not relabel ordinary tasks as decisions.
3. **Follow-ups:** obligations where the owner is blocking someone, open waiting-on items due or stale, and any preparation needed for the next consequential meeting.

Then add only sections that contain real signal: project changes, stakeholder context, calendar shape, an acceleration idea, or a weekly expectations check. Merge repeated items instead of restating them in several sections. Give credit by name when supported. If the base is sparse, show the few known actions and the missing context plainly; do not fill the page with placeholders or generic productivity advice.

For each action, say **who**, **what**, and **when** if known. Keep facts separate from recommendations. A recommendation should explain the evidence behind it in one short line. Apply the owner's voice guide, and do not use em dashes.

## Deliver

- Generate readable, mobile-friendly HTML with inline CSS and no required external assets. Make the top actions visible without scrolling on a typical desktop screen. Escape untrusted text from files and connectors before inserting it into HTML.
- Write only the brief, the auto-generated region of `me/index.md` when it needs refreshing, and a dated `me/log.md` entry when `me/` exists. Do not change project, people, decision, or waiting-on records.
- Open the HTML if supported. In chat, give the top action and a clickable path to the artifact; do not repeat the entire brief.
