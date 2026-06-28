# INIT: Set Up This Personal OS

You are the AI agent reading this file. Your job is to **interview the owner and populate their
Personal OS**, turning the `[PLACEHOLDER]` templates under `me/` into a real, personalized base. Follow
this script top to bottom. Do not rush; this is a conversation, not a form.

> If you are the human reading this: open your AI agent in this folder and say
> *"Read INIT.md and set me up."* Then just answer the questions.

## Operating Rules For This Onboarding

- **Ask one question at a time.** Wait for the answer before moving on. Keep it conversational.
- **Offer to infer.** If the owner says "you decide" or gives you a resume, LinkedIn text, or a brain
  dump, draft the file content yourself and show it for a yes/no.
- **Write as you go.** After each section, fill the matching file(s) and tell the owner what you wrote.
  Do not wait until the end to write everything.
- **Confirm before writing.** Show the content you intend to write, then write on approval.
- **Honor the conventions:** date and attribute entries, no em-dashes in any drafted content, drafts
  not sends.
- **It is fine to skip.** If the owner does not have a team, or only one project, skip the parts that
  do not apply and note it.

## Before You Start

1. Read `CONTEXT.md` so you understand the layers, the file schemas, and the conventions.
2. Skim the `_TEMPLATE.md` files in `me/projects/`, `me/stakeholders/top/`, and `me/team/` so you know
   the exact frontmatter and headings to produce.
3. Greet the owner, explain in two sentences what a Personal OS is, and tell them the interview takes
   about 15 to 20 minutes and they can stop or skip anytime.

## The Interview

Go layer by layer. For each step: ask the questions, then fill the listed file(s).

### Step 1 - Identity basics

Ask: name, the role/title, the company or context, and how they would describe what they are
responsible for in one or two sentences.

Then write:

- `me/index.md` - set owner, role, the one-paragraph operating picture, and a one-line "current theme."
- `me/profile.md` - name, role, working style, anything notable about how they operate.
- `me/role.md` and `me/role-expectations.md` - the role and what success in it looks like.

### Step 2 - Voice and how they are judged

Ask:

- How do they want to come across in writing to (a) their team, (b) executives, (c) a public/brand
  audience? Any hard style rules (for example: lead with a TL;DR, always name the owner of a next
  action)?
- What is the story they want people to tell about them when they are not in the room? Two or three
  threads. Any catchphrases. Any anti-patterns they want to avoid.
- How are they evaluated? What are the two to four pillars their performance is judged on?

Then write:

- `me/communications.md` - the three registers, the hard rules, and one or two worked examples in
  their voice (draft these from what they told you).
- `me/personal-narrative.md` - the threads, catchphrases, anti-patterns, and a source-attribution
  table (date the entries to today).
- `me/expectations.md` - the leadership/role pillars and any per-stakeholder expectations.

### Step 3 - Direction

Ask:

- What is the single most important thing they are driving end to end right now? What does "done"
  look like, what is the live blocker, and what is the next move?
- What are this week's top three or four outcomes? Any personal focus for the week?
- What are their durable six-to-twelve-month goals?
- Any standing guidance from their leadership they want to keep front of mind?

Then write:

- `me/current-drive.md` - fill the `## Narrative` one-liner, the `period` frontmatter, the live
  blocker, and the next move; the brief renders these as its banner.
- `me/weekly-goals.md` (set `week_of` to this week's Monday), `me/long_term_goals.md`,
  `me/exec_steer.md`.
- Leave `me/waiting-on.md` and `me/log.md` empty; they fill up through daily use.

### Step 4 - Projects

For each active project (aim for the top three to five, not everything):

Ask: name, a one-line description, current status, priority (P0 to P3), who the key people are, which
stakeholders care, and how closely they want it tracked (full, selective, passive).

Then write one `me/projects/<slug>.md` per project using `me/projects/_TEMPLATE.md`. Use a short
kebab-case slug for the filename and set `aliases` to the natural ways they refer to the project (these
drive `/debrief` routing, so be generous).

### Step 5 - Stakeholders

For each key stakeholder (the people they manage upward or across to):

Ask: name, role, which projects connect you, what matters most to them, any patterns in how they make
decisions, and anything they are currently waiting on from the owner.

Then write one `me/stakeholders/top/<slug>.md` per person using the stakeholder template. Put
secondary contacts in `me/stakeholders/other/`. Set `aliases`.

### Step 6 - Team

For each direct report or close collaborator:

Ask: name, level, what they own, their strengths, where they want to grow, and any recent feedback.

Then write one `me/team/<slug>.md` per person using the team template. Set `manager` to the owner's
slug and set `aliases`.

### Step 7 - Update config

Ask which stakeholders the weekly/monthly status drafts should cover by default. Write those slugs into
`me/updates/config.md`.

## Finish

1. **Clean up the examples.** Once the owner has at least one real project, stakeholder, and team file,
   delete the `EXAMPLE-*.md` files (confirm first). If a folder would be left empty, keep its
   `_TEMPLATE.md` and `.gitkeep`.
2. **Scan for leftovers.** Grep the `me/` tree for `[PLACEHOLDER`, `[YOUR_`, and `TODO`. Report any
   file still holding template text so the owner can finish it later.
3. **Show the result.** Summarize what you created: how many projects, stakeholders, and team files,
   and which files still need attention.
4. **Hand off.** Tell the owner what to do next:
   - Run `/brief` to generate their first morning brief.
   - At the end of the day, run `/debrief` and paste a dump of what happened.
   - Weekly, run `/os-review` and `/weekly-status`.
   - Read `MANUAL.md` for the full workflow and how to extend the system.

## Tune The Skills After A Few Days

Tell the owner this explicitly, then move on: the `/brief` and `/debrief` skills ship with sensible
defaults, but they are meant to be edited. After running the loop for a few days, open
`.claude/skills/brief/SKILL.md` and `.claude/skills/debrief/SKILL.md` and adjust them to fit how the
owner actually works. Common tweaks:

- **Brief:** reorder or drop sections; change the acceleration check to the owner's own signature
  lens; set per-project `coverage` defaults; wire up connectors (Slack, Gmail, Calendar); or point the
  skill at a script-based HTML renderer for speed.
- **Debrief:** add routing keywords and aliases the owner actually uses; adjust which nuggets count as
  update-worthy; enable meeting-notes enrichment if a provider is available.

If the owner has their own polished brief or debrief implementation, this is where it drops in.

That is it. The base gets sharper every time they debrief, and the skills get sharper every time they
tune them.
