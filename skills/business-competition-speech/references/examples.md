# 调用、压缩和预算示例

这些示例展示工作方法，不是固定 rubric 或必须套用的稿件。新比赛的评分表、用户指令和最终 Excel 优先；不要把案例品牌、目标或模拟预算带入其他项目。

## 三个可直接修改的调用

### 1. Rubric 与 Excel 齐全时写完整稿

```text
$business-competition-speech
请根据我附上的比赛 brief、完整 rubric 和最终预算 Excel，写一份 Senior 难度的英文演讲稿。
按我指定的 Part 顺序写连贯正文，总长不超过 580 English words；以 125 words per minute 加 15 秒停顿估算，不超过 5 分钟。
先在内部逐项映射 rubric，确保每点都有观点、机制和结果，前后 Part 自然承接。
预算必须与 Excel 的总额、分项、单位、天数、排名和 savings 完全一致，解释 how spent、top two costs、attractiveness、competitiveness、budget constraints 和两个不同的 savings。
Brand Value 必须覆盖 two values、engagement、sales vs brand experience、brand identity 和 market image。
Conclusion 简短回扣 Feasibility、Competitiveness 和 Attractiveness；如果本次 rubric 要求主体详述，先完成主体要求。
交付可直接口播的正文，并在末尾简短标明字数、时长假设和预算核对状态。
```

### 2. 转为 Junior，保留论证和数字

```text
$business-competition-speech
把下面这份已完成的稿子改为 Junior 英语。用常见词、短句和明确连接词，保留原 Part 顺序和每个评分点的逻辑闭环。
所有预算数字、单位、目标和统计分母保持不变；two values、two savings、brand identity、market image 以及 engagement 的行为、机制和测量都必须保留。
不要只换简单词却删掉 why/how，也不要增加新事实。仍需满足我给出的字数和时限；如存在冲突，指出具体冲突。
默认只给修改后的口播正文；字数或时间存在实质问题时再简短说明。
【在此附原稿、rubric、最终 Excel 和字数/时间要求】
```

### 3. 最小改动压缩，至少减少 30 个英文词

```text
$business-competition-speech
对下面英文稿做最小改动，至少减少 30 English words。保留原 Part、顺序、语气、所有数字、独特证据和完整得分点，不要整篇重写。
先删重复、装饰语和无评分作用的细节，再合并句子。不能把两个 values 或两个 savings 缩成一个，也不能删掉 comparison、voting、purchase、measurement、brand identity 或 market image 等已要求的内容。
如果原稿本来缺少当前 rubric 的必要点，只补最短必要句，并把新增文字算入最终净减少量。
用同一计数口径核对前后实际口播正文，给出原字数、新字数和净减少量；不足 30 不算完成。
【在此附原稿和当前 rubric；预算段另附最终 Excel】
```

## Brand Value：来自用户的原稿与新推导的压缩稿

以下原稿来自本次提供的缓存对话中用户粘贴的英文段落。压缩稿在此重新推导，不能把历史 assistant 的缩短版本当作评分标准。当前要求明确包括 market image，而原稿没有直接说明，因此压缩稿补上最短必要表达，并把它算入净减少量。

### 用户提供的原稿

First, it creates measurable commercial value. Two-hour flavor drops create urgency, tasting reduces uncertainty, and the Flavor Passport guides customers from curiosity to comparison, voting, and purchase.

Our three-day targets are 3,000 visitors, 1,800 tasting participants, 1,050 completed Flavor Passports, 900 opt-in profiles, and 660 transactions or preorders, equal to a 22 percent conversion rate. Entry counts, QR records, voting data, and checkout results will measure engagement and sales.

Second, it creates long-term brand value by making YEAH GELATO’s product method visible. The brand emphasizes traditional hand-finishing, fresh ingredients, on-site production, and a new flavor every two hours. Our live kitchen, ingredient map, and freshness clock turn these principles into an experience customers can understand and remember.

The concept therefore focuses on both selling products and creating a brand experience. Customers can taste and buy limited batches, while also learning why the product is fresh and contributing ideas for future flavors.

### 新推导的压缩稿

First, it creates measurable commercial value. Two-hour flavor drops create urgency, tasting reduces uncertainty, and the Flavor Passport guides comparison, voting, and purchase.

Our three-day targets are 3,000 visitors, 1,800 tasting participants, 1,050 completed Flavor Passports, 900 opt-in profiles, and 660 transactions or preorders: a 22 percent conversion rate. Entry counts, QR records, voting data, and checkout results measure engagement and sales.

Second, it creates long-term brand value. The live kitchen, ingredient map, and freshness clock show YEAH GELATO’s traditional hand-finishing, fresh ingredients, on-site production, and a new flavor every two hours, shaping a fresh, transparent market image customers can remember.

The concept supports both sales and brand experience: customers taste and buy limited batches, understand freshness, and suggest future flavors.

按本 Skill 的 [计数工具](../scripts/measure_speech.py) 对上述两个**仅含英文口播正文**的 UTF-8 文件实际测量：原稿 **151 words**，压缩稿 **121 words**，净减少 **30 words**；`--min-reduction 30 --exact-words 121` 检查通过，退出码为 `0`。这里的连字符词算一个词，`1,050` 等数字算一个数字 token，不推测数字实际读法；若比赛规定展开数字口播，先将两个计数文件按实际读法改写，再重新计数。此处不是实测演讲时长。

保留的逻辑是：限时新品和试吃降低购买阻力，护照引导 comparison、voting、purchase，目标与记录方式衡量参与及销售；现场制作、原料图和新鲜时钟呈现四项品牌特征，并支持 fresh / transparent 的市场形象。稿件明确选择 sales 与 brand experience 两者兼顾。22 percent 是 `660 ÷ 3,000` 的目标转化率，不能误写成实际成绩或改用试吃人数作分母。

这只是对用户已明确要求的压缩示范，不构成对未提供的完整官方 rubric 或 Excel 的验证。

## Budget：模拟输入账本与配套口播

**以下是独立的合成案例，全部数字为演示设定，不来自真实 Excel，也未做真实工作簿验证。** 场景为三天活动；这个 100 m² 场地不代表上文 YEAH GELATO 项目的面积。真实任务必须读取用户最终工作簿。

| 模拟输入项目 | 最终费用（CNY） | 已给定的用途或计费口径 |
| --- | ---: | --- |
| Equipment / materials | 10,000 | 现场制作设备、原料与试吃用品 |
| Staff | 8,000 | 制作、引导试吃比较与投票、协助数字反馈 |
| Venue | 6,000 | 20 CNY / m² / day × 100 m² × 3 days |
| Modular fixtures | 3,000 | 租用同规格稳固模块设施 |
| Digital feedback | 1,000 | 数字投票和反馈记录 |
| **总支出** | **28,000** | 上述五项相加 |
| **预算上限** | **30,000** | 给定约束 |
| **未分配余量** | **2,000** | 上限减总支出；不是另加的支出项 |

| 已采用的两项 savings | 同口径原方案（CNY） | 最终方案（CNY） | 已实现的差额（CNY） | 质量保护 |
| --- | ---: | ---: | ---: | --- |
| 买模块设施改为租用 | 4,000 | 3,000 | 1,000 | 使用相同稳固规格，保护展示和动线功能 |
| 纸质反馈改为数字反馈 | 1,500 | 1,000 | 500 | 保留相同投票选项和记录，并由人员协助使用 |

两项 savings 共 **1,500 CNY**，已经反映在最终 **28,000 CNY** 中，不再从总额扣一次。模拟账本的最高两项确实是 equipment / materials **10,000 CNY** 和 staff **8,000 CNY**。

### 配套英文口播示范

Our three-day plan spends CNY 28,000 against a CNY 30,000 ceiling, leaving CNY 2,000 of unallocated headroom. We spend CNY 10,000 on equipment and materials for live preparation and tasting, CNY 8,000 on staff to guide comparisons and voting, CNY 6,000 on the venue, CNY 3,000 on modular fixtures, and CNY 1,000 on digital feedback. Venue cost is CNY 20 per square meter per day for 100 square meters across three days. The two highest costs are the equipment and materials category and the staff category: reliable production supports fresh samples, while guided service turns curiosity into participation and purchase. Visible preparation and tasting make the event attractive and give customers a clear reason to choose the experience. We protect this competitive strength within the ceiling by saving CNY 1,000 through renting fixtures for CNY 3,000 instead of purchasing them for CNY 4,000, with the same sturdy specifications. We save another CNY 500 by using CNY 1,000 digital feedback instead of CNY 1,500 paper feedback, with staff support preserving access and accurate records. Both savings are already included in CNY 28,000 and are not deducted again.

示例说明 how spent、真实 top two 及理由、吸引力来源、竞争优势、预算上限和余量，以及两个不同且保护核心体验的 savings。实际调用应按用户时限继续压缩，不能把示例长度当作要求。

## 缺少工作簿时的反例

只有旧稿或用户口述总额，没有最终 Excel 时，以下说法不合格：

> 所有预算数字已经与 Excel 完全一致；设备与人员就是最高两项；两个 savings 已验证。

它虚构了核对状态、排序和节省额。可完成独立的文字工作，并明确报告：

> 当前未提供最终 Excel。预算总额、分项、计费口径、最高两项及 savings 尚未核对；现有数字只能标为来自所给稿件或口述，不能标为 Excel 已验证。其余 Part 可以先按已提供的要求完成。

获得工作簿后再检查数据、公式、排名和 savings 是否已计入最终总额，然后更新预算正文与核对状态。
