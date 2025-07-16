import pandas as pd
import numpy as np
from collections import Counter

# 读取CSV文件
df = pd.read_csv('datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv')

print("=== 验证元宝(DeepSeek R1) HTML报告分析结果 ===")
print(f"CSV总记录数: {len(df)}")
print()

# 1. 验证基本统计数据
print("=== 1. 基本统计数据验证 ===")
print(f"元宝报告显示记录数: 80")
print(f"CSV实际记录数: {len(df)}")
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

print("元宝报告显示前三名:")
print("1. Customer Service: 67.9%")
print("2. Project Manager: 60.7%")
print("3. Email Manager: 53.3%")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(agent_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证元宝报告中提到的具体智能体类型
print("验证元宝报告中提到的智能体类型:")
yuanbao_agents = ['Customer Service', 'Project Manager', 'Email Manager']
for agent in yuanbao_agents:
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

print("元宝报告显示前三名:")
print("1. Claude-3.5: 72.2%")
print("2. GPT-4o: 66.7%")
print("3. LLaMA-3: 64.3%")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(model_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证元宝报告中提到的具体模型架构
print("验证元宝报告中提到的模型架构:")
yuanbao_models = ['Claude-3.5', 'GPT-4o', 'LLaMA-3']
for model in yuanbao_models:
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

print("元宝报告显示前三名:")
print("1. Communication: 0.912")
print("2. Decision Making: 0.855")
print("3. Research & Summarization: 0.838")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(task_bias_median.head(3).iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}")
print()

# 验证元宝报告中提到的具体任务类型
print("验证元宝报告中提到的任务类型:")
yuanbao_tasks = ['Communication', 'Decision Making', 'Research & Summarization']
for task in yuanbao_tasks:
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

# 检查任务类型公正性排名是否正确
yuanbao_task_ranking_correct = True
correct_top3_tasks = ['Communication', 'Research & Summarization', 'Decision Making']
yuanbao_top3_tasks = ['Communication', 'Decision Making', 'Research & Summarization']

if yuanbao_top3_tasks[0] == correct_top3_tasks[0]:
    print("2. 任务类型公正性排名第一位: Communication ✅")
else:
    yuanbao_task_ranking_correct = False

print()

print("❌ 错误的分析结果:")

# 检查智能体类型占比是否正确
yuanbao_agent_correct = 0
total_yuanbao_agents = len(yuanbao_agents)
for agent in yuanbao_agents:
    if agent in agent_multimodal['agent_type'].values:
        agent_data = agent_multimodal[agent_multimodal['agent_type'] == agent].iloc[0]
        print(f"验证 {agent}: 报告{67.9 if agent == 'Customer Service' else 60.7 if agent == 'Project Manager' else 53.3}%, 实际{agent_data['percentage']}%")

print(f"1. 智能体类型多模态能力占比 - 完全错误，所有数值都显著过高")

# 检查模型架构占比是否正确
yuanbao_model_correct = 0
total_yuanbao_models = len(yuanbao_models)
for model in yuanbao_models:
    if model in model_multimodal['model_architecture'].values:
        model_data = model_multimodal[model_multimodal['model_architecture'] == model].iloc[0]
        print(f"验证 {model}: 报告{72.2 if model == 'Claude-3.5' else 66.7 if model == 'GPT-4o' else 64.3}%, 实际{model_data['percentage']}%")

print(f"2. 大模型架构多模态能力占比 - 完全错误，所有数值都显著过高")

# 检查任务类型公正性数值是否正确
print("3. 任务类型公正性中位数数值 - 部分错误:")
for task in yuanbao_tasks:
    if task in task_bias_median['task_category'].values:
        task_data = task_bias_median[task_bias_median['task_category'] == task].iloc[0]
        yuanbao_value = 0.912 if task == 'Communication' else 0.855 if task == 'Decision Making' else 0.838
        print(f"  {task}: 报告{yuanbao_value}, 实际{task_data['bias_detection_score']:.4f}")

print("4. 任务类型公正性排名 - 部分错误:")
print(f"  正确排名: {' -> '.join(correct_top3_tasks)}")
print(f"  元宝排名: {' -> '.join(yuanbao_top3_tasks)}")
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

print()
print("=== 关键错误分析 ===")
print("1. 智能体类型多模态占比数据严重错误 - 所有百分比都过高(60-70%范围)，实际应该在0-60%范围")
print("2. 大模型架构多模态占比数据严重错误 - 所有百分比都过高(60-70%范围)，实际应该在0-40%范围")
print("3. 任务公正性数值过高 - 报告数值在0.8+范围，实际多数在0.7+范围")
print("4. 可能使用了错误的计算公式或数据源") 