---
name: eli5
description: Make a picture-first HTML explanation of any topic with a real diagram, plain language, and source boundaries. Use when the owner invokes /eli5 or asks for a visual explainer, simple diagram walkthrough, or explain-like-I'm-five page.
argument-hint: "<topic or source path> (optional audience)"
---

# Visual ELI5

Create a self-contained HTML page that helps a newcomer understand the requested topic. The topic can be general, technical, or drawn from this workspace. A useful diagram is required every time; decorative art does not count.

## Understand first

Identify the key parts, their relationship, and the one idea the reader should remember. Read any supplied files. For a workspace explanation, trace claims to actual files rather than guessing from names. Research current or uncertain claims with available sources. If a source is unavailable, narrow the claim and mark the uncertainty. Do not copy a community skill or imply that this skill is endorsed by Anthropic.

## Build the page

Write `explainers/YYYY-MM-DD-<slug>.html` using a short, safe slug; add a numeric suffix if that file already exists. The page should work offline and contain no external fonts, images, scripts, stylesheets, trackers, or runtime fetches. Use semantic HTML, inline CSS, and an inline SVG with a title and description. Escape all text taken from files or web pages before inserting it into HTML.

Put the main diagram near the top. Choose a flow, timeline, comparison, feedback loop, or concept map that shows the actual relationship. Label nodes and arrows in plain words, make the reading direction obvious, and keep text readable on mobile. Add a short text sequence below the SVG so the explanation still works without the diagram. Use `<details>` only if a deeper layer genuinely helps; JavaScript is not needed.

Below the diagram, provide:

- a short walkthrough in everyday language;
- one analogy that clarifies the mechanism, followed by one sentence saying where the analogy stops working;
- a compact source list for material claims, with file paths or clickable URLs and dates where relevant. Mark an unsourced conceptual example as an example, not a verified fact.

Keep wording simple without talking down to the reader. Prefer concrete nouns and verbs. Avoid unnecessary jargon; define any term that remains. Do not use em dashes. The page should be useful to someone who has not seen the conversation.

Open the file when supported. In chat, give the one-sentence takeaway and a link to the HTML page. Do not write to `me/`, update the ledger, or send anything externally as part of an explanation.
