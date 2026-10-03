# independent-review-gate（独立验收闸门）

一个 agent skill，让"做完了"不再等于"我自己看了一遍"。三部分：把验收标准写成能跑的脚本；交给另一个只读、没见过你推理的对抗性审稿会话；人只裁决取舍。

改编自 Anthropic [Claude-shaped science](https://www.anthropic.com/research/claude-shaped-science) 一文的做法。首次用在一份多页合同上：脚本抓到 1 个问题，独立审稿人另抓到 25 个，几乎不重合。

## 安装

把整个文件夹复制到你的 agent 技能目录：

```bash
# Claude Code
cp -R independent-review-gate ~/.claude/skills/
# Codex
cp -R independent-review-gate ~/.codex/skills/
```

新开一个会话即可生效。中文版：`SKILL.zh.md`（内容相同）。

## 用法

让你的 agent 在宣布交付物完成前先跑一遍，例如："对这份报告用 independent-review-gate"。它会基于 `scripts/check_example.py` 写检查脚本并运行，用 `templates/reviewer-prompt.md` 开一个独立审稿会话，最后只把需要人裁决的问题交给你。

## 文件

- `SKILL.md` / `SKILL.zh.md`：skill 本体（英文 / 中文）
- `templates/reviewer-prompt.md`：独立审稿人的提示词模板
- `scripts/check_example.py`：验收脚本骨架（示例数据是玩具，改 RULES 部分）

## 局限

审稿人给的是线索，不是判决。法律、医疗、财务问题仍需专业人士。MIT 协议。
