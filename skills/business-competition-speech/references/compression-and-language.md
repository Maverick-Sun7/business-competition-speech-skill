# 最小修改、语言等级与限制

## 原稿保护

用户说“改少一点”而上下文是内容太长，做最小范围压缩，不另写一个新方案。若上下文是上一版改动幅度太大，减少改写范围。结合上下文判断，不机械把两种意思混同。

锁住 Part 顺序、已正确的事实、用户喜欢的表达、rubric 子点、两个 strengths/values/savings、关键机制与结果、Excel 数字和单位。外部材料的最新更正若要求变更事实，只改相关位置及其依赖，不能擅自换整套概念。

删字后“每个得分点还在”需要重新验证。压缩版虽更短，若删掉对 comparison、market image、how spent 或每项 quality protection 的解释，就应修复。

## 压缩程序

1. 按同一口径统计原稿。提取口播正文；是否包含 Part 标题以实际口播为准，不把核查表计入。
2. 删除无评分作用的细节、背景、修辞和重复 signposting。
3. 收紧句子，合并同一机制的因果与结果，保留两个独立评分点的辨识度。
4. 检查内部覆盖表和所有数字；若某句承担多个点，确认它们仍各自完整。
5. 精确复算。`at least 30 fewer words` 是 before − after ≥ 30；`under 420` 与 `no more than 420` 分别是 <420 和 ≤420。精确词数、区间和相对减少不能互相代替。

若用户同时给减少量和总字数，以两项都满足为目标。不能靠删除标题、添加标点、滥用连字符或数字缩写制造虚假压缩。超紧限制下，先给最短完整稿并具体指出还差多少，以及进一步压缩将损失哪个点。

通常只附一句真实统计，例如“原稿 176 words，新稿 142 words，减少 34”；先运行计数再填写，示例数字不能照抄。

## Junior / Senior

| Junior | Senior | 恒定内容 |
|---|---|---|
| 常见动词、短句、每句少量概念 | 商业表达更精确，允许合并句子 | 全部 rubric 子要求 |
| because / so / this helps 等明确连接 | 可用自然的因果与功能连接 | 主张、机制、结果 |
| 必要术语随句解释 | 术语保留但避免堆砌 | 证据、指标、数字、限制 |

Senior 示例：“Timed flavor releases encourage repeat visits, while visible preparation supports a freshness-led identity.”

Junior 示例：“We offer a new flavor at set times, so visitors have a reason to return. They can also watch us prepare the product. This shows that freshness is part of our brand.”

若原 rubric 要求 market image，二者都还需说明形成什么预期市场印象；上述两句本身不自动覆盖它。

## 字数与时间

计数工具使用 UTF-8 纯正文。English 模式统计 Latin/数字 token；内部 apostrophe/hyphen 可作为同一 token，数值小数点和千位逗号不拆词。`two-hour` 与 `22%` 各按一个 token；数字不会自动展开。比赛有官方计数规则时，以官方规则为准并另作核查；不能说工具等同任何比赛软件。

中文模式为非空白、非标点的 Unicode 字符计数，包含字母与数字；mixed 为英语 token 加 Han 字符。三种口径不混用。混合稿应说明比赛如何计数；工具的默认口径不能创造官方规则。

用于计时的文字先按实际念法展开数字，例如 `3,000` → `three thousand`；只念正文时排除标题、脚注和说明。English 时长估算：words ÷ WPM × 60 + pause seconds。用用户实际排练语速；缺少语速时明确假设，工具默认 120 WPM 只是估算参数，不是 Junior/Senior 标准。留出用户实际需要的转场/停顿，不能保证某个通用速度人人可达。

示例：

```bash
python3 scripts/measure_speech.py after.txt --before before.txt --min-reduction 30 --max-words 420
python3 scripts/measure_speech.py spoken.txt --minutes 3 --wpm 120 --pause-seconds 8
python3 scripts/measure_speech.py chinese.txt --mode chinese --max-words 500
```

`--max-words` 在非 English 模式限制该模式的计数单位。`--exact-words` 与它互斥。退出码 0 表示所提供限制通过，1 表示至少一个限制失败，2 表示参数/输入错误。工具只能检查这些机械限制，不能认证评分覆盖、真实口播能力或预算一致性。
