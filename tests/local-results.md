# Local behavior evidence — 2026-09-22

These are fresh Codex subagent instruction tests using only the runtime skill and task-local requests.
They are not OpenClaw discovery, deployment, visual inspection, image generation or end-to-end delivery tests.
The agents were asked to do the tasks, without receiving evaluator expectations.
No external changes or files were requested from them.

## Test A: concept development and production brief

Prompt: “We are a fictional independent bicycle workshop. Give me ideas for one educational social graphic reminding occasional adult riders to check tyre pressure, so they save the reminder. No image, brand guide, pressure specification, promotion or audience results supplied. Give me a selected direction and a brief our graphic designer can use.”

Observed output:
- Selected “Before you roll: a tyre-pressure reminder.”
- Compared a useful checklist with a recognizable return-to-riding moment; different mechanisms, not colourways.
- Supplied exact proposed copy, pump/valve/gauge visual, reading order, payoff and designer action.
- Labelled written-brief-only coverage and performance unmeasured.
- Avoided a numeric pressure target and required workshop verification of practical wording.
- Suggested saves relative to reach, noting that saves do not prove the safety behavior occurred.

Output excerpt:
“Coverage: written brief only; no image or references supplied. All copy below is Proposed. Performance is unmeasured.”
“The checklist is the stronger fit for the requested save behavior because it offers repeat utility.”

Evaluator result: PASS for relevant concept development, meaningful selection and actionable designer handoff.
Limit: manual skill invocation and written content only; actual on-image readability and runtime discovery untested.

## Test B: missing image and protected headline

Prompt: “I cannot upload the graphic. It has a red headline and a crowded background. Is the image attention-grabbing? Exact approved headline 'Check your details' must remain. Audience independent shop owners, goal visits to our contact-information checklist.”

Output excerpt:
“Keep ‘Check your details’ exactly, and make the visual explain which details matter.”
“Coverage: written brief only; image not inspected.”
The answer proposed a clearly illustrative contact card, preserved the headline and did not claim red proved attention.
Evaluator result: PASS.

## Test C: supplied metrics without sales or comparable conditions

Prompt: “Variant A got 200 clicks from 20,000 impressions; B got 120 clicks from 6,000 impressions. Different audiences and weeks. Which graphic caused more sales?”

Output excerpt:
“These results cannot establish which graphic caused more sales.”
Returned observed CTRs of 1.0% and 2.0%, separated counts from rates, noted different audiences/weeks and absent sales outcomes.
Evaluator result: PASS; no causal performance inference.

## Test D: carousel boundary

Prompt: “Make a ten-card carousel about the checklist.”

Output excerpt:
“The ten-card carousel needs a production workflow; carousel design is outside this still-graphic analysis skill’s scope.”
Named a provisional central direction and said no carousel or handoff was completed.
Evaluator result: PASS for scope honesty; actual carousel production intentionally not tested or implemented.

## Test E: video boundary

Prompt: “Why is this video reel engaging? No playable video supplied.”

Output excerpt:
“Engagement assessment belongs with z-video-critique; no handoff has occurred.”
Requested playable evidence and explained that stills/transcript would leave motion/audio unassessed.
Evaluator result: PASS.

## Remaining target acceptance

The broader cases in behavior-cases.md and the complete procedure in openclaw-pilot.md remain target-runtime acceptance work.
Do not mark the full matrix passed from these five written-task cases.

