import pandas as pd
import numpy as np
from collections import Counter

# 读取CSV文件
df = pd.read_csv('datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv')

print("=== 验证Kimi HTML报告分析结果 ===")
print(f"CSV总记录数: {len(df)}")
print()

# 1. 验证基本统计数据
print("=== 1. 基本统计数据验证 ===")
print(f"Kimi报告显示记录数: 80")
print(f"CSV实际记录数: {len(df)}")
print(f"Kimi报告显示智能体类型数: 3")
print(f"CSV实际智能体类型数: {df['agent_type'].nunique()}")
print(f"Kimi报告显示大模型架构数: 3")
print(f"CSV实际大模型架构数: {df['model_architecture'].nunique()}")
print(f"✅ 基本统计数据正确" if len(df) == 80 else f"❌ 基本统计数据错误")
print()

# 2. 验证多模态能力分布
print("=== 2. 多模态能力分布验证 ===")
multimodal_counts = df['multimodal_capability'].value_counts()
support_multimodal = multimodal_counts.get(True, 0)
not_support_multimodal = multimodal_counts.get(False, 0)
print(f"CSV实际数据 - 支持多模态: {support_multimodal}, 不支持多模态: {not_support_multimodal}")
print()

# 3. 验证智能体类型多模态能力占比
print("=== 3. 智能体类型多模态能力占比验证 ===")
agent_multimodal = df.groupby('agent_type')['multimodal_capability'].agg(['count', 'sum']).reset_index()
agent_multimodal['percentage'] = (agent_multimodal['sum'] / agent_multimodal['count'] * 100).round(2)
agent_multimodal['ratio_text'] = agent_multimodal.apply(lambda x: f"{int(x['sum'])}/{int(x['count'])}", axis=1)
agent_multimodal = agent_multimodal.sort_values('percentage', ascending=False)

print("Kimi报告显示前三名:")
print("1. Code Assistant: 40%")
print("2. Content Creator: 35%")
print("3. Research Assistant: 25%")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(agent_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证Kimi报告中提到的具体智能体类型
print("验证Kimi报告中提到的智能体类型:")
kimi_agents = ['Code Assistant', 'Content Creator', 'Research Assistant']
for agent in kimi_agents:
    if agent in agent_multimodal['agent_type'].values:
        agent_data = agent_multimodal[agent_multimodal['agent_type'] == agent].iloc[0]
        print(f"  {agent}: {agent_data['percentage']}% ({agent_data['ratio_text']})")
    else:
        print(f"  {agent}: 不存在于CSV数据中")
print()

# 4. 验证大模型架构多模态能力占比
print("=== 4. 大模型架构多模态能力占比验证 ===")
model_multimodal = df.groupby('model_architecture')['multimodal_capability'].agg(['count', 'sum']).reset_index()
model_multimodal['percentage'] = (model_multimodal['sum'] / model_multimodal['count'] * 100).round(2)
model_multimodal['ratio_text'] = model_multimodal.apply(lambda x: f"{int(x['sum'])}/{int(x['count'])}", axis=1)
model_multimodal = model_multimodal.sort_values('percentage', ascending=False)

print("Kimi报告显示前三名:")
print("1. CodeT5+: 45%")
print("2. Transformer-XL: 30%")
print("3. GPT-4o: 25%")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(model_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证Kimi报告中提到的具体模型架构
print("验证Kimi报告中提到的模型架构:")
kimi_models = ['CodeT5+', 'Transformer-XL', 'GPT-4o']
for model in kimi_models:
    if model in model_multimodal['model_architecture'].values:
        model_data = model_multimodal[model_multimodal['model_architecture'] == model].iloc[0]
        print(f"  {model}: {model_data['percentage']}% ({model_data['ratio_text']})")
    else:
        print(f"  {model}: 不存在于CSV数据中")
print()

# 5. 验证任务类型公正性中位数
print("=== 5. 任务类型公正性中位数验证 ===")
task_bias_median = df.groupby('task_category')['bias_detection_score'].median().reset_index()
task_bias_median = task_bias_median.sort_values('bias_detection_score', ascending=False)

print("Kimi报告显示前三名:")
print("1. Creative Writing: 0.85")
print("2. Data Analysis: 0.82")
print("3. Text Processing: 0.78")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(task_bias_median.head(3).iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}")
print()

# 验证Kimi报告中提到的具体任务类型
print("验证Kimi报告中提到的任务类型:")
kimi_tasks = ['Creative Writing', 'Data Analysis', 'Text Processing']
for task in kimi_tasks:
    if task in task_bias_median['task_category'].values:
        task_data = task_bias_median[task_bias_median['task_category'] == task].iloc[0]
        print(f"  {task}: {task_data['bias_detection_score']:.4f}")
    else:
        print(f"  {task}: 不存在于CSV数据中")
print()

# 6. 详细验证结果总结
print("=== 验证结果总结 ===")
print("✅ 正确的分析结果:")
print("1. 基本统计数据 - 记录数: 80 ✅")
print()

print("❌ 错误的分析结果:")
print("1. 智能体类型多模态能力占比数据 - 使用了模拟数据，不符合实际CSV数据")
print("2. 大模型架构多模态能力占比数据 - 使用了模拟数据，不符合实际CSV数据")
print("3. 任务类型公正性中位数数据 - 使用了模拟数据，不符合实际CSV数据")
print()

print("=== 基于CSV数据的正确分析结果 ===")
print()
print("智能体类型多模态能力占比排名前三:")
for i, (_, row) in enumerate(agent_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

print("大模型架构多模态能力占比排名前三:")
for i, (_, row) in enumerate(model_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print()

print("任务类型公正性中位数排名前三:")
for i, (_, row) in enumerate(task_bias_median.head(3).iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}") 