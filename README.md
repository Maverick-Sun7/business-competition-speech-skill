# Business Competition Speech Skill

为商业比赛演讲稿与预算配套输出设计的可复用 Codex Skill。以 rubric 为写作骨架，把每个评分点写成最小逻辑闭环，支持 Junior/Senior 英语和最小改动压缩。

Skill 名称：`business-competition-speech`。建议仓库名：`business-competition-speech-skill`；仓库名与调用名不同，调用时使用后者。

公开仓库：[Maverick-Sun7/business-competition-speech-skill](https://github.com/Maverick-Sun7/business-competition-speech-skill)。

## 它解决什么

- 按实际 rubric 拆分并覆盖所有子要求，用“行动/主张 → 理由/机制 → 结果”检查论证。
- 按 Part 写可口播的完整段落，前后能力、体验、预算与品牌价值互相支撑。
- Junior/Senior 只调整语言，不减少评分点；压缩优先删重复、修辞和非评分细节。
- 预算核对总额、单位、公式、周期、真实 top two、余额与 savings；逐项解释 how spent、importance、attractiveness、competitiveness、constraints 和两项节省的质量保护。
- Brand Value 分别覆盖 two values、engagement、sales/brand experience、brand identity 与 market image。
- Conclusion 简短回扣 Feasibility、Competitiveness、Attractiveness；当前 rubric 有更具体要求时遵循当前要求。
- 工具可精确计数及检查“至少减少 30 words”，并按明确语速与停顿估算时长。

不预设品牌、地点、面积、预算数字或官方分值；缺原始 rubric/Excel 时会标明核验范围，不能保证评分或假称数字已核实。

## 目录

```text
business-competition-speech-skill/
├── README.md
├── .gitignore
└── skills/
    └── business-competition-speech/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── rubric-and-logic.md
        │   ├── budget-integrity.md
        │   ├── compression-and-language.md
        │   ├── examples.md
        │   └── source-notes.md
        └── scripts/
            └── measure_speech.py
```

主指令只保留共同约束；按任务读取参考文件。覆盖表用于内部核查，不能代替口播正文。

## 安装和使用

下载或克隆本仓库，将完整 `skills/business-competition-speech/` 文件夹复制到 Codex 的 skills 目录。默认位置是 `~/.codex/skills/`；若自定义了 `CODEX_HOME`，使用其 `skills/` 子目录。已存在同名 Skill 时先比较文件，再做有意的更新，避免意外覆盖。

在 Codex 中可以明确使用 `$business-competition-speech`。UI 元数据保留自动发现的默认行为，没有设成仅显式调用。只运行计数脚本需 Python 3.9+，不需要安装第三方库；实际 Excel 读写由运行 Skill 的环境提供 spreadsheet 工具或库。

建议输入：实际评分表、比赛 brief、最新预算 Excel、原稿（若有）、语言等级、Part/成员分工、字数与时间限制。已有信息不必重复给。

### 写全文并配预算

```text
使用 $business-competition-speech。
根据附件 rubric、brief 和 final-budget.xlsx，写 Senior 英语比赛稿。
按给定 Part 成文，总计不超过 600 words；实际口播不超过 5 分钟。
预算说明覆盖 how spent、top two costs、吸引力、竞争力、预算取舍和两项节省。
Brand Value 覆盖 two values、engagement、sales vs experience、identity、market image。
先核对 Excel，再给可口播正文和简短核验结果。
```

### 最小改动压缩

```text
使用 $business-competition-speech。
下面英文稿至少减少 30 words，只做必要修改。
保留 Part、顺序、原来的主要表达和全部评分点；数字与附件 Excel 一致。
给压缩稿，并报告同一口径的原/新字数与净减少量。
[粘贴原稿]
```

### 改成 Junior

```text
使用 $business-competition-speech。
把这篇 Senior 稿转为 Junior 英语，保留全部理由、结果、指标与预算解释。
总计不超过 420 words；Conclusion 保持简短。
[提供原稿与 rubric]
```

可复制的完整输入/输出与合成预算示例见 [examples.md](skills/business-competition-speech/references/examples.md)。

## 字数和时间工具

从仓库根目录运行；输入应只包含实际口播文字。数字用于计时前按实际念法展开。标题、说明和表格若包含在文件里也会计数，工具不会猜哪些文字要念。

```bash
python3 skills/business-competition-speech/scripts/measure_speech.py after.txt --before before.txt --min-reduction 30 --max-words 420
python3 skills/business-competition-speech/scripts/measure_speech.py spoken.txt --minutes 3 --wpm 120 --pause-seconds 8
python3 skills/business-competition-speech/scripts/measure_speech.py chinese.txt --mode chinese --max-words 500
```

输出 JSON，包含计数口径、前后计数、减少量、检查结果和时长假设。退出码：`0` 检查通过，`1` 限制未满足，`2` 参数或文件错误。`--exact-words` 可检查精确计数；`--help` 查看完整选项。

英语按 Latin/数字 token 计数，内部 apostrophe/hyphen 和数值逗号/小数点不拆词；中文按非空白非标点字符计数，mixed 按英语 token 加 Han 字符计数。比赛有官方口径时用官方规则再核对。时长是估算，最终实际时间需排练确认。工具不自动判断 rubric 覆盖或 Excel 是否一致。

## 预算配套的核验方式

先锁定最终 workbook，检查公式与计算结果，记录稿中数字对应的单元格，确认计费单位与周期，再排序 top two。节省已进入表内总额时，不再次扣除。两个 savings 各解释如何保护核心质量。

输出预算表时保持表与稿共享同一最终数字；只改稿时不擅改 workbook。缺 workbook 或公式无法重算时明确“未完成 Excel 核验”，仍可继续文字修改。

## 来源与当前边界

本版本依据用户明确确认的写作要求及《写稿服务详解》可读的最近五轮片段蒸馏。原始评分表、Excel 和更早 samples 未由接口提供，不能声称已读全历史。具体来源边界见 [source-notes.md](skills/business-competition-speech/references/source-notes.md)。公开包仅收录规则与已标明的示范，不含原始聊天导出或实际比赛 workbook。

可用原始 rubric、Excel 和后续修改反馈逐步更新这个 Skill。更新时先复查已有约束，再补缺失规则，不把单个案例数字或临时偏好升级为通用要求。
