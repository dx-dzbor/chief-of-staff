# Onboard your chief of staff

For Claude Code, run `/onboard` after cloning. In another agent, say: **"Read `INIT.md` and onboard me."** This is a short first session, not a form to complete. Ask one question at a time, accept a rough dump, and skip anything the owner does not know. Resume later without repeating answered questions.

## Prepare a private workspace

`templates/me/` contains public starter files and fictional examples. Before writing personal context, run `python3 scripts/bootstrap_me.py`. It checks Git privacy, copies starters into `me/` without overwriting, skips `EXAMPLE-*.md`, and keeps `_TEMPLATE.md` files for future projects and people. If Python is unavailable, copy those files with the agent's file tools and perform the same checks. If an older checkout tracks `me/`, follow the migration in `MANUAL.md` and keep the owner's existing files intact.

Create or resume `me/onboarding.md` with a simple stage (`questions`, `review`, or `ready`), the last completed question, and any unfinished follow-up. This file is private. If `me/` already contains real context, inspect it first and ask only what is missing. If it is already ready, ask what the owner wants to change rather than restarting the interview. Never replace real facts with template placeholders.

## Ask only what creates a useful first brief

Open with one sentence: "I'll learn what you own, what matters now, and your next move, then make a first brief." Ask these questions one at a time. Use information already supplied instead of asking it again.

1. **Work:** "What do you do at work, and who depends on you? A rough dump is fine."
2. **Outcome:** "What one outcome matters most in the next two weeks? What would done look like, and is there a date?"
3. **Next move:** "What's blocking it, and what's the next concrete action? Who owns that action?"

If a critical detail is missing, ask one short follow-up. A user can say "skip" or pause at any point. Do not require a company name, org chart, writing sample, connector, or complete project list. Do not infer a deadline or assign an owner without evidence.

## Confirm the first operating picture

Reflect back the owner's role, outcome, next action, owner, date if known, and any uncertainty in a few lines. Show the exact proposed changes to `me/index.md`, `me/current-drive.md`, and `me/weekly-goals.md`, plus `me/profile.md` or `me/role.md` only where facts support them. If a named project needs its own file to make the brief useful, propose one file from `me/projects/_TEMPLATE.md`. Ask the owner to correct or accept this picture before writing it. Keep unanswered template fields out of active summaries; leave them for later.

After acceptance, write the supported content, set `me/onboarding.md` to `ready`, and run `/brief` immediately. If there is too little information for a concrete priority, ask for the missing action before making the brief. Report the files created and the top action. No external message is sent.

## Offer one useful routine

After the first brief, ask: "Would a weekday morning brief help, or would another recurring check be more useful?" The command works manually without scheduling. Only if the owner opts in, ask for time and timezone. Prefer a **local Claude Desktop scheduled task** pointing at this folder, since the private `me/` files live here. Use a prompt such as: "In this folder, run `/brief` for today. Use local `me/` context, save the HTML brief, and report the top action and link. Do not send messages." Create it when the current agent supports local scheduled tasks; otherwise give the owner those exact settings. Do not set up a cloud routine against the public template because it would not see local `me/` files. Do not schedule a task without the owner's choice of time.

## Grow only when useful

Later debriefs and requests can add real projects, stakeholders, team members, decisions, voice examples, and status audiences. Ask for one missing detail only when it would change the current output. The templates under `templates/me/` and `CONTEXT.md` define the formats; `MANUAL.md` explains the daily loop.
