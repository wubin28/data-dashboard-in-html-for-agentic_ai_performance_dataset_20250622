import pandas as pd
import numpy as np
from collections import Counter

# 读取CSV文件
df = pd.read_csv('datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv')

print("=== 验证豆包HTML报告分析结果 ===")
print(f"CSV总记录数: {len(df)}")
print()

# 1. 验证基本统计数据
print("=== 1. 基本统计数据验证 ===")
print(f"豆包报告显示记录数: 80")
print(f"CSV实际记录数: {len(df)}")
print(f"✅ 基本统计数据正确" if len(df) == 80 else f"❌ 基本统计数据错误")
print()

# 2. 验证多模态能力分布
print("=== 2. 多模态能力分布验证 ===")
multimodal_counts = df['multimodal_capability'].value_counts()
support_multimodal = multimodal_counts.get(True, 0)
not_support_multimodal = multimodal_counts.get(False, 0)

print(f"豆包报告显示 - 支持多模态: 9, 不支持多模态: 79")
print(f"CSV实际数据 - 支持多模态: {support_multimodal}, 不支持多模态: {not_support_multimodal}")
print(f"✅ 多模态分布正确" if support_multimodal == 9 and not_support_multimodal == 79 else f"❌ 多模态分布错误")
print()

# 3. 验证智能体类型多模态能力占比
print("=== 3. 智能体类型多模态能力占比验证 ===")
agent_multimodal = df.groupby('agent_type')['multimodal_capability'].agg(['count', 'sum']).reset_index()
agent_multimodal['percentage'] = (agent_multimodal['sum'] / agent_multimodal['count'] * 100).round(2)
agent_multimodal['ratio_text'] = agent_multimodal.apply(lambda x: f"{int(x['sum'])}/{int(x['count'])}", axis=1)
agent_multimodal = agent_multimodal.sort_values('percentage', ascending=False)

print("豆包报告显示前三名:")
print("1. Research Assistant: 75% (3/4)")
print("2. Code Assistant: 33.33% (1/3)")
print("3. Content Creator: 33.33% (1/3)")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(agent_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证Research Assistant的具体数据
research_assistant_data = df[df['agent_type'] == 'Research Assistant']
ra_total = len(research_assistant_data)
ra_multimodal = research_assistant_data['multimodal_capability'].sum()
ra_percentage = (ra_multimodal / ra_total * 100) if ra_total > 0 else 0

print(f"Research Assistant详细验证:")
print(f"豆包报告: 75% (3/4)")
print(f"CSV实际: {ra_percentage:.2f}% ({ra_multimodal}/{ra_total})")
print(f"✅ Research Assistant正确" if ra_percentage == 75 and ra_total == 4 else f"❌ Research Assistant错误")
print()

# 4. 验证大模型架构多模态能力占比
print("=== 4. 大模型架构多模态能力占比验证 ===")
model_multimodal = df.groupby('model_architecture')['multimodal_capability'].agg(['count', 'sum']).reset_index()
model_multimodal['percentage'] = (model_multimodal['sum'] / model_multimodal['count'] * 100).round(2)
model_multimodal['ratio_text'] = model_multimodal.apply(lambda x: f"{int(x['sum'])}/{int(x['count'])}", axis=1)
model_multimodal = model_multimodal.sort_values('percentage', ascending=False)

print("豆包报告显示前三名:")
print("1. GPT-4o: 42.86% (3/7)")
print("2. CodeT5+: 33.33% (2/6)")
print("3. Transformer-XL: 28.57% (2/7)")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(model_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证GPT-4o的具体数据
gpt4o_data = df[df['model_architecture'] == 'GPT-4o']
gpt4o_total = len(gpt4o_data)
gpt4o_multimodal = gpt4o_data['multimodal_capability'].sum()
gpt4o_percentage = (gpt4o_multimodal / gpt4o_total * 100) if gpt4o_total > 0 else 0

print(f"GPT-4o详细验证:")
print(f"豆包报告: 42.86% (3/7)")
print(f"CSV实际: {gpt4o_percentage:.2f}% ({gpt4o_multimodal}/{gpt4o_total})")
print(f"✅ GPT-4o正确" if abs(gpt4o_percentage - 42.86) < 0.1 and gpt4o_total == 7 else f"❌ GPT-4o错误")
print()

# 5. 验证任务类型公正性中位数
print("=== 5. 任务类型公正性中位数验证 ===")
task_bias_median = df.groupby('task_category')['bias_detection_score'].median().reset_index()
task_bias_median = task_bias_median.sort_values('bias_detection_score', ascending=False)

print("豆包报告显示前三名:")
print("1. Communication: 0.8214")
print("2. Learning & Adaptation: 0.7910")
print("3. Text Processing: 0.7657")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(task_bias_median.head(3).iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}")
print()

# 验证具体的中位数值
communication_median = df[df['task_category'] == 'Communication']['bias_detection_score'].median()
learning_median = df[df['task_category'] == 'Learning & Adaptation']['bias_detection_score'].median()
text_median = df[df['task_category'] == 'Text Processing']['bias_detection_score'].median()

print(f"Communication中位数验证:")
print(f"豆包报告: 0.8214")
print(f"CSV实际: {communication_median:.4f}")
print(f"✅ Communication正确" if abs(communication_median - 0.8214) < 0.0001 else f"❌ Communication错误")
print()

print(f"Learning & Adaptation中位数验证:")
print(f"豆包报告: 0.7910")
print(f"CSV实际: {learning_median:.4f}")
print(f"✅ Learning & Adaptation正确" if abs(learning_median - 0.7910) < 0.0001 else f"❌ Learning & Adaptation错误")
print()

print(f"Text Processing中位数验证:")
print(f"豆包报告: 0.7657")
print(f"CSV实际: {text_median:.4f}")
print(f"✅ Text Processing正确" if abs(text_median - 0.7657) < 0.0001 else f"❌ Text Processing错误")
print()

# 显示完整的任务类型公正性排名
print("=== 完整任务类型公正性中位数排名 ===")
for i, (_, row) in enumerate(task_bias_median.iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}")
print()

# 显示完整的智能体类型多模态占比
print("=== 完整智能体类型多模态占比排名 ===")
for i, (_, row) in enumerate(agent_multimodal.iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 显示完整的模型架构多模态占比
print("=== 完整模型架构多模态占比排名 ===")
for i, (_, row) in enumerate(model_multimodal.iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print() 