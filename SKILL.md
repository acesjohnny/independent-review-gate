---
name: independent-review-gate
description: Use before declaring any important deliverable "done" (a contract, report, curriculum, data table, script, batch of media) or whenever you, the agent, are about to say "done". Runs a three-part gate: (1) write the acceptance standard as an executable check script, (2) hand the finished product to a separate, read-only adversarial reviewer session that never saw your reasoning, (3) let the human rule on trade-offs the reviewer surfaces. Also use to judge whether a task is machine-checkable enough to hand to an agent at scale.
---

# Independent Review Gate

Adapted from the workflow Matthew Schwartz described in Anthropic's "Claude-shaped science" post (2026-10): pick problems whose results a machine can check, write the success criteria as code, give the work to an adversarial reviewer, keep the human for taste and trade-offs.
Source: https://www.anthropic.com/research/claude-shaped-science

**One line:** acceptance standard as runnable code; the product reviewed by a session that never saw your reasoning; the human rules only on trade-offs. The drafter re-reading its own work does not count as review.

In a first real run on a multi-page contract, the script caught 1 issue and an independent reviewer caught 25 more, with almost no overlap. Do both.

## When to use / not use

- Use: deliverables others will rely on (contracts, client reports, lesson plans, data tables, batch scripts, media batches), and any moment you are about to say "done".
- Skip: one-off tiny edits, chat answers, exploratory drafts. For small things, just apply the self-check list below.
- First ask: can a machine verify this? Numbers that can be recomputed, reruns, line-by-line comparison against a source: good, let the agent scale. Only taste can judge it: keep a human in the loop.

## The four steps (each leaves a file behind)

1. **Write the acceptance standard (the human sets it; the drafter does not grade itself).**
   - List the decisions, red lines, and conventions: what must appear, what must not remain (old addresses, old account numbers, `TODO` markers), how numbers add up, which cross-references must exist, whether counts are self-consistent.
   - Save it as a script file, not a one-liner. See `scripts/check_example.py` for a skeleton: must-contain, must-not-contain, sum checks, invariants (e.g. refund <= amount paid), cross-reference existence, exported copies (docx/pdf) matching the source.
   - Run it and fix failures. Do not say "done" until it passes.
2. **Independent review.**
   - Spawn a separate read-only subagent/session. Give it only: path to the product, the standard, the review dimensions, the output format. Do not give it your reasoning, your rationale, or the weaknesses you already know about.
   - Use `templates/reviewer-prompt.md`. It tells the reviewer: you did not draft this, do not defend it, read-only, mark uncertainty as "unsure", invent no facts outside the standard, list what you could not verify.
   - Fixed dimensions: A check against the standard; B internal consistency (amounts, currency, dates, cross-references, who the subject of each duty is); C risk (ambiguity, one-sidedness, logic conflicts, capacity to sign); D exported files match the source.
   - Do not send confidential originals to an external online reviewer; a local subagent is fine.
3. **Human ruling.**
   - Sort findings into: factual errors (fix directly), business trade-offs (list options with a recommendation, ask the human), and professional judgement (legal, medical, financial: not the agent's call).
   - Ask only what needs ruling, with a recommendation each. Do not hand over 25 raw findings.
   - Back up the original before editing.
4. **Re-review and record.**
   - After edits, rerun the script, then start a new reviewer session that is told what was ruled and asked only: fixed correctly? fixed completely? any new conflicts? Cap at 2 re-review rounds by default; the human may ask for more, and remaining disagreements go to the human.
   - Leave a short record (what was done, script N items / M failed, reviewer found X, Y rulings pending).

## Drafter self-check (known agent habits from the source article)

- Never claim "done (with one asterisk)": an asterisk means not done. List what is not done.
- Time estimates are unreliable: report what is done and not done, not precise durations.
- On a slow job, ask whether a small tool can compress the work before brute-forcing it.
- "Looks consistent" is not verification: show script output or a page/figure a human looked at.
- Do not rename a forbidden move to get around it (forbid "unproven lemma", get a new "axiom").
- Your own script can miss things. Passing it does not replace step 2.

## Reviewers also err

Treat reviewer output as leads, not verdicts. Check each against the source text before adopting. A reviewer cannot verify business facts the standard does not contain (prices, rankings, registrations, account numbers); keep its "could not verify" list in your report verbatim.

## Report format when finished

Only: script N items / M failed; reviewer found X (Y must-fix); which rulings were applied; what is still pending with the human; what was not verified. If not finished, say where it is stuck.
