# independent-review-gate

An agent skill that stops "done" from meaning "I re-read my own work." Three parts: an acceptance standard written as a runnable script, a separate read-only adversarial reviewer that never saw your reasoning, and a human who rules only on trade-offs.

Adapted from the workflow in Anthropic's [Claude-shaped science](https://www.anthropic.com/research/claude-shaped-science) post. Tried first on a multi-page contract: the script found 1 problem, an independent reviewer found 25 more, almost no overlap.

## Install

Copy this folder into your agent's skills directory:

```bash
# Claude Code
cp -R independent-review-gate ~/.claude/skills/
# Codex
cp -R independent-review-gate ~/.codex/skills/
```

Start a new session so the skill is picked up. Chinese version: `SKILL.zh.md` (same content).

## Use

Ask your agent to run the gate before it calls a deliverable finished, e.g. "use independent-review-gate on this report". It will write a check script from `scripts/check_example.py`, run it, spawn a reviewer using `templates/reviewer-prompt.md`, and bring you only the decisions that need a human.

## Files

- `SKILL.md` / `SKILL.zh.md`: the skill (English / Chinese)
- `templates/reviewer-prompt.md`: prompt for the independent reviewer
- `scripts/check_example.py`: skeleton acceptance script (toy example; edit the RULES section)

## Limits

A reviewer is a source of leads, not a verdict. Legal, medical, and financial points still need a professional. MIT licensed.
