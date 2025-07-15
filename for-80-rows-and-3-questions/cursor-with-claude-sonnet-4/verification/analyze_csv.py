import pandas as pd
import numpy as np
from collections import Counter

# 读取CSV文件
df = pd.read_csv('datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv')

print("=== CSV数据基本信息 ===")
print(f"总记录数: {len(df)}")
print(f"总列数: {len(df.columns)}")
print()

# 验证基本统计数据
print("=== 基本统计数据验证 ===")
print(f"处理数据记录数: {len(df)}")
print(f"智能体类型数量: {df['agent_type'].nunique()}")
print(f"大模型架构数量: {df['model_architecture'].nunique()}")
print(f"任务类型数量: {df['task_category'].nunique()}")
print()

# 显示具体的类型
print("智能体类型列表:")
agent_types = df['agent_type'].value_counts()
for agent_type, count in agent_types.items():
    print(f"  {agent_type}: {count}")
print()

print("大模型架构列表:")
model_archs = df['model_architecture'].value_counts()
for model_arch, count in model_archs.items():
    print(f"  {model_arch}: {count}")
print()

print("任务类型列表:")
task_categories = df['task_category'].value_counts()
for task_category, count in task_categories.items():
    print(f"  {task_category}: {count}")
print()

# 验证多模态能力总览
print("=== 多模态能力总览验证 ===")
multimodal_counts = df['multimodal_capability'].value_counts()
print(f"支持多模态 (TRUE): {multimodal_counts.get(True, 0)}")
print(f"不支持多模态 (FALSE): {multimodal_counts.get(False, 0)}")
print()

# 验证智能体类型多模态能力占比
print("=== 智能体类型多模态能力占比验证 ===")
agent_multimodal = df.groupby('agent_type')['multimodal_capability'].agg(['count', 'sum']).reset_index()
agent_multimodal['percentage'] = (agent_multimodal['sum'] / agent_multimodal['count'] * 100).round(1)
agent_multimodal['ratio_text'] = agent_multimodal.apply(lambda x: f"{int(x['sum'])}/{int(x['count'])}", axis=1)
agent_multimodal = agent_multimodal.sort_values('percentage', ascending=False)

print("智能体类型多模态能力占比排名:")
for i, (_, row) in enumerate(agent_multimodal.iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证大模型架构多模态能力占比
print("=== 大模型架构多模态能力占比验证 ===")
model_multimodal = df.groupby('model_architecture')['multimodal_capability'].agg(['count', 'sum']).reset_index()
model_multimodal['percentage'] = (model_multimodal['sum'] / model_multimodal['count'] * 100).round(1)
model_multimodal['ratio_text'] = model_multimodal.apply(lambda x: f"{int(x['sum'])}/{int(x['count'])}", axis=1)
model_multimodal = model_multimodal.sort_values('percentage', ascending=False)

print("大模型架构多模态能力占比排名:")
for i, (_, row) in enumerate(model_multimodal.iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证任务类型公正性中位数
print("=== 任务类型公正性中位数验证 ===")
task_bias_median = df.groupby('task_category')['bias_detection_score'].median().reset_index()
task_bias_median = task_bias_median.sort_values('bias_detection_score', ascending=False)

print("任务类型公正性(bias_detection_score)中位数排名:")
for i, (_, row) in enumerate(task_bias_median.iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}")
print()

# 显示每个任务类型的详细统计
print("=== 任务类型公正性详细统计 ===")
for task_category in df['task_category'].unique():
    subset = df[df['task_category'] == task_category]['bias_detection_score']
    print(f"{task_category}: 中位数={subset.median():.4f}, 平均值={subset.mean():.4f}, 数量={len(subset)}")
print() 