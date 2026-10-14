---
name: business-competition-speech
description: 撰写、审核和最小改动压缩商业比赛演讲稿及预算说明，严格映射 rubric、保留评分点逻辑闭环、按 Part 成文、缩放 Junior/Senior 英语，并核对 Excel 数字与字数时长。适用于商赛提案与品牌快闪演讲，不用于一般营销文案。
---

# 商业比赛演讲稿与预算

把评分要求写成能直接口播的论证。优先级是评分覆盖、事实与预算一致、限制满足、语言自然；高级词汇不能替代解释。

## 先确定任务和权威材料

识别模式：新写、评分检查、预算配套、Junior/Senior 转换、局部最小修改、压缩。沿用用户已给的信息，不重复索取。

提取当前 rubric、比赛 brief、原稿、最新 Excel 及版本、Part/分工、语言等级、字数和时限、用户确认的更正。当前材料和明确指令优先于旧例与本 Skill 的结构惯例。若指令与实际 rubric 或数字相冲突，指出具体冲突，继续能独立完成的部分；不得声称冲突两端均已满足。

原始 rubric 缺失时，以用户已明确列出的要求起草并标明“按所列要求核查”；不能宣称官方 rubric 全覆盖。Excel 缺失时可改文字，但预算标为未验证，不编造数值、排名或 savings。样稿的品牌、地点、面积、指标只属于该例，不能自动套用。

## 用评分点组织论证

先在内部建立覆盖表：评分点原文/子要求 → 来源 → 对应 Part 与句子 → 观点 → 机制或理由 → 结果 → 所需证据/数字 → 状态。拆开 rubric 的复合要求和数量要求，特别是 two、why、how、both、constraints。

每点至少形成“具体主张或行动 → 为什么有效 → 对本评分点的结果”。一句可以承担多个点，前提是每个点都可独立辨认其闭环。仅出现关键词、报数字、写“提升品牌价值”或“有竞争力”不算完成。需要测量时给指标、分母、记录方式，并区分目标与已发生结果。

正文按用户指定的 Part 写连贯段落，不能把 rubric 改成编号清单或 bullet list。Part 内用简短 signposting；用上一段的行动或结果引出下一段。自然链路通常是 agency 能力 → concept/客户路径 → 投入怎样支持路径 → engagement/sales/brand outcomes → 简短结论。用户指定的 Part 顺序优先，不固定 Part 数量。

完整覆盖与闭环标准见 [references/rubric-and-logic.md](references/rubric-and-logic.md)。进行评分检查、新写全文或修改相关 Part 时读取。

## 不能漏掉的核心要求

- **Agency / concept**：若 rubric 要求 specialization、two strengths、team roles、location/scale/duration 或体验路径，逐项覆盖。Specialization 要解释做什么及作用；每个 strength 都说明怎样区别于竞争者及为什么有效，不编造竞争者事实。
- **Budget**：total budget、how spent、真实 top two costs 各自为何重要、投入怎样支持 attractiveness 与 competitiveness、怎样平衡 customer appeal 和 budget constraints、两个不同的 savings 及各自为何不降低核心体验/质量。数字、货币、单位、计费周期、公式、排序、余额和节省额与 Excel 一致。
- **Brand Value**：两个可区分的 values 各有闭环；engagement 包含行为、机制与测量；明确选择 selling products / brand experience / both 并解释；分别说明 brand identity 如何被体现，以及目标市场将形成什么 market image。商业价值与长期品牌价值是可用例子，实际 rubric 对 two values 的定义优先。
- **Conclusion**：通常用很短的句子分别触及 Feasibility、Competitiveness、Attractiveness，并回扣正文已有证据。不要另开大 Part 或重复主体分析。若当前 rubric 明确要求主体详述这些点，按当前 rubric 完成后再简短收尾。

预算任务必须读取 [references/budget-integrity.md](references/budget-integrity.md)。涉及实际 `.xlsx` 的读写，使用目标环境可用的 spreadsheet 工具或库；该参考包含独立于工具的核对流程，不能仅看截图或凭经验乘天数。

## 控制语言、字数和修改范围

Junior 使用常见词、短句、明确因果；Senior 可更精炼商业化，但评分点、证据、两个 values、两个 savings、数值和因果强度完全保留。不要把 Junior 理解为减少内容。

“最小改动”保护原来的 Part、顺序、语气、核心表达和已正确的事实，只改为满足新要求所必需的句子。“少一点/至少少 30”在英语稿上下文按 English words 计，先确认可见上下文，使用同一计数口径核对原稿和新稿；中文稿区分字符，不混算。默认保留稿中独特的评分证据，不因能在别处找到就随意删掉。

压缩顺序：无评分作用的细节与装饰语 → 重复 → 可缩短的例子 → 合并机制与结果 → 简化句法。每轮重新查覆盖表，保护因果、数量要求、专有名词与数字。不能为了达到数字删除评分点。若最短完整稿仍超限，具体说明冲突和当前最短完整稿，不偷偷漏点或声称完成。

涉及压缩、难度转换、时长时读取 [references/compression-and-language.md](references/compression-and-language.md)。用 [scripts/measure_speech.py](scripts/measure_speech.py) 对只含实际口播正文的 UTF-8 文本计数；Part 标题是否口播按比赛规则决定。数字先按打算说出的形式写入计时文本。工具不能自动核查 rubric 或 Excel。

有字数上限和时限时两者都检查。时长 = 口播 words / 实际或明确假设的 words per minute + 停顿/切换时间；标为估算，给语速和停顿假设。没有录音或排练不能声称实测达标。

## 交付前检查

1. 各评分点都有句子和闭环；两个要求没有缩成一个泛泛理由；前后 Part 承接自然。
2. 所有数字对照同一最终 Excel 与事实表；不存在旧面积、旧地点、旧总额或重复扣 savings。
3. Junior/Senior 难度、净减少量、字数/时长限制满足；最小修改未变成整篇重写。
4. 结论有依据且简短；去掉无效背景、重复卖点和无支撑比较。

默认给用户可直接口播的 Part 正文；仅在有用时附很短的字数/时长/预算状态。用户只要稿子时不附检查过程。用户要预算表或核查报告时单独交付，不把表格或列表混入口播正文。存在实质未验证项必须明确说明，不能隐藏。

实际调用、示例与反例见 [references/examples.md](references/examples.md)，只在需要模板或示范时读取。来源边界见 [references/source-notes.md](references/source-notes.md)；它不是新的 rubric。
