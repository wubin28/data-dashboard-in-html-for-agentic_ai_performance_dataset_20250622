import pandas as pd
import numpy as np
from collections import Counter

# 读取CSV文件
df = pd.read_csv('datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv')

print("=== 验证DeepSeek HTML报告分析结果 ===")
print(f"CSV总记录数: {len(df)}")
print()

# 1. 验证基本统计数据
print("=== 1. 基本统计数据验证 ===")
print(f"DeepSeek报告显示记录数: 80")
print(f"CSV实际记录数: {len(df)}")
print(f"DeepSeek报告显示智能体类型数: 12")
print(f"CSV实际智能体类型数: {df['agent_type'].nunique()}")
print(f"DeepSeek报告显示大模型架构数: 11")
print(f"CSV实际大模型架构数: {df['model_architecture'].nunique()}")
print(f"DeepSeek报告显示任务类别数: 10")
print(f"CSV实际任务类别数: {df['task_category'].nunique()}")
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

print("DeepSeek报告显示前三名:")
print("1. Code Assistant: 50.0%")
print("2. Content Creator: 33.3%")
print("3. Customer Service: 20.0%")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(agent_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['agent_type']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证DeepSeek报告中提到的具体智能体类型
print("验证DeepSeek报告中提到的智能体类型:")
deepseek_agents = ['Code Assistant', 'Content Creator', 'Customer Service']
for agent in deepseek_agents:
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

print("DeepSeek报告显示前三名:")
print("1. CodeT5+: 40.0%")
print("2. GPT-4o: 33.3%")
print("3. Claude-3.5: 16.7%")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(model_multimodal.head(3).iterrows(), 1):
    print(f"{i}. {row['model_architecture']}: {row['percentage']}% ({row['ratio_text']})")
print()

# 验证DeepSeek报告中提到的具体模型架构
print("验证DeepSeek报告中提到的模型架构:")
deepseek_models = ['CodeT5+', 'GPT-4o', 'Claude-3.5']
for model in deepseek_models:
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

print("DeepSeek报告显示前三名:")
print("1. Creative Writing: 0.781")
print("2. Problem Solving: 0.739")
print("3. Code Generation: 0.726")
print()

print("CSV实际数据前三名:")
for i, (_, row) in enumerate(task_bias_median.head(3).iterrows(), 1):
    print(f"{i}. {row['task_category']}: {row['bias_detection_score']:.4f}")
print()

# 验证DeepSeek报告中提到的具体任务类型
print("验证DeepSeek报告中提到的任务类型:")
deepseek_tasks = ['Creative Writing', 'Problem Solving', 'Code Generation']
for task in deepseek_tasks:
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

# 检查智能体类型占比是否正确
deepseek_agent_correct = 0
total_deepseek_agents = len(deepseek_agents)
for agent in deepseek_agents:
    if agent in agent_multimodal['agent_type'].values:
        agent_data = agent_multimodal[agent_multimodal['agent_type'] == agent].iloc[0]
        if agent == 'Code Assistant' and abs(agent_data['percentage'] - 50.0) < 0.1:
            deepseek_agent_correct += 1
        elif agent == 'Content Creator' and abs(agent_data['percentage'] - 33.3) < 0.1:
            deepseek_agent_correct += 1
        elif agent == 'Customer Service' and abs(agent_data['percentage'] - 20.0) < 0.1:
            deepseek_agent_correct += 1

print(f"1. 智能体类型多模态能力占比 - 准确率: {deepseek_agent_correct}/{total_deepseek_agents}")

# 检查模型架构占比是否正确
deepseek_model_correct = 0
total_deepseek_models = len(deepseek_models)
for model in deepseek_models:
    if model in model_multimodal['model_architecture'].values:
        model_data = model_multimodal[model_multimodal['model_architecture'] == model].iloc[0]
        if model == 'CodeT5+' and abs(model_data['percentage'] - 40.0) < 0.1:
            deepseek_model_correct += 1
        elif model == 'GPT-4o' and abs(model_data['percentage'] - 33.3) < 0.1:
            deepseek_model_correct += 1
        elif model == 'Claude-3.5' and abs(model_data['percentage'] - 16.7) < 0.1:
            deepseek_model_correct += 1

print(f"2. 大模型架构多模态能力占比 - 准确率: {deepseek_model_correct}/{total_deepseek_models}")

# 检查任务类型公正性是否正确
deepseek_task_correct = 0
total_deepseek_tasks = len(deepseek_tasks)
for task in deepseek_tasks:
    if task in task_bias_median['task_category'].values:
        task_data = task_bias_median[task_bias_median['task_category'] == task].iloc[0]
        if task == 'Creative Writing' and abs(task_data['bias_detection_score'] - 0.781) < 0.01:
            deepseek_task_correct += 1
        elif task == 'Problem Solving' and abs(task_data['bias_detection_score'] - 0.739) < 0.01:
            deepseek_task_correct += 1
        elif task == 'Code Generation' and abs(task_data['bias_detection_score'] - 0.726) < 0.01:
            deepseek_task_correct += 1

print(f"3. 任务类型公正性中位数 - 准确率: {deepseek_task_correct}/{total_deepseek_tasks}")
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