---
name: debrief
description: Capture a free-form day dump, route clear facts into the Personal OS, and review material or uncertain changes before applying them. Use for /debrief, end-of-day capture, or wrapping up the day.
argument-hint: "(optional) day dump"
---

# Debrief

Keep the original account of the day, update clear routine facts, and put consequential or uncertain edits in front of the owner. No message is sent externally.

## Capture and route

If `me/` does not exist and a dump was supplied, bootstrap private `me/` as in `INIT.md`, save the raw dump verbatim under `me/debriefs/`, then use it as initial `/onboard` context so the owner does not repeat it. Do not route inferred facts until onboarding confirms the operating picture. If no dump was supplied, start `/onboard`. Never save personal text under public `templates/me/`.

Use inline arguments as the dump. Otherwise ask for the day's notes in one short sentence and wait. Save the supplied text verbatim in `me/debriefs/YYYY-MM-DD.md`, appending under a time heading if the file exists. Do not polish the raw text. If the owner explicitly asks for a dry run or no write, show the proposed routing without saving anything.

Read `me/index.md`, aliases in real project and people files, `me/waiting-on.md`, and `me/decisions.md`. Skip templates and examples. Match aliases case-insensitively, prefer exact or longest matches, and route to multiple files only when the text really concerns multiple entities. Optional meeting notes can add candidates, but mark their source and put them through review before writing because the owner did not supply them directly. If a source fails, continue with the dump.

Apply **routine capture** directly when the text and destination are clear: append dated factual notes to existing project, stakeholder, and team histories; record clearly attributed stakeholder advice or feedback; and append concrete `shipped`, `progress`, `win`, `risk`, `ask`, or `narrative` nuggets to `me/updates/raw/YYYY-MM.md`. Preserve meaning and attribution. Do not turn speculation into a fact or invent a date, owner, result, or metric.

Hold **material or uncertain changes** for review. This includes new or changed decisions in `me/decisions.md`; opening, clearing, or changing a commitment in `me/waiting-on.md`; rewriting current project state or next steps; changing frontmatter; creating a project or person file; ambiguous alias matches; and any inferred claim that could misstate what happened. An unmatched line stays in the raw dump and is listed as unresolved; it is never silently dropped.

## Decision records

Record an explicit decision only after review. Use `me/decisions.md` as the current state and the update ledger as the dated event trail. Give each decision the next free `D-YYYYMMDD-NN` ID. Include date, decision, source, and `owner`, `next`, and `checkpoint` when known; use `none` otherwise. Add a brief rationale only if the source supports it. Keep active records newest first. When closing one, preserve the original record and add the close date, outcome, and source. Do not treat a proposal or discussion as a settled decision.

## Review and finish

After routine writes, report them briefly. Show each pending change with its exact destination, proposed text, source, and why review is needed. Offer **Approve**, **Edit**, or **Skip**. Apply only approved items; an edit gets a revised proposal before writing. Skipping leaves the raw dump and routine capture in place. If nothing is pending, finish without an approval step.

Refresh only the auto-generated region of `me/index.md` if approved entity changes require it. Append a dated `me/log.md` entry summarizing written and pending counts; if pending items are approved later, append a follow-up log entry rather than rewriting history. End with a compact account of what was saved and what still needs the owner's decision, plus the raw debrief path.
