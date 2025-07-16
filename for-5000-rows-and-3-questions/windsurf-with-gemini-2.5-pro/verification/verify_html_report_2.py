import pandas as pd
import numpy as np

def analyze_csv_data_detailed():
    # Read the CSV file
    df = pd.read_csv('datasets/agentic_ai_performance_dataset_20250622.csv')
    
    print("=== CSV数据分析和HTML报告验证 (第二份报告) ===")
    print(f"总记录数: {len(df)}")
    print()
    
    # Question 1: Agent Types with Highest Multimodal Capability
    print("1. 各智能体类型多模态能力占比Top 3")
    print("=" * 60)
    
    # Calculate multimodal capability percentage by agent type
    agent_multimodal = df.groupby('agent_type').agg({
        'multimodal_capability': ['count', 'sum']
    })
    agent_multimodal.columns = ['total_count', 'multimodal_count']
    agent_multimodal['multimodal_percentage'] = (agent_multimodal['multimodal_count'] / agent_multimodal['total_count'] * 100).round(2)
    agent_multimodal = agent_multimodal.sort_values('multimodal_percentage', ascending=False)
    
    print("实际的前10名智能体类型多模态能力占比:")
    print(agent_multimodal[['total_count', 'multimodal_count', 'multimodal_percentage']].head(10))
    print()
    
    print("HTML报告声称的前3名:")
    print("- Code Assistant: 100.00%")
    print("- Translation Agent: 100.00%") 
    print("- Content Creator: 100.00%")
    print()
    
    # Check specific agent types mentioned in HTML
    print("检查HTML报告中提到的具体智能体类型:")
    for agent_type in ['Code Assistant', 'Translation Agent', 'Content Creator']:
        if agent_type in agent_multimodal.index:
            row = agent_multimodal.loc[agent_type]
            print(f"- {agent_type}: {row['multimodal_percentage']:.2f}% (实际数据)")
        else:
            print(f"- {agent_type}: 未在数据中找到")
    print()
    
    # Question 2: Model Architectures with Highest Multimodal Support
    print("2. 各大模型架构多模态能力占比Top 3")
    print("=" * 60)
    
    # Calculate multimodal capability percentage by model architecture
    model_multimodal = df.groupby('model_architecture').agg({
        'multimodal_capability': ['count', 'sum']
    })
    model_multimodal.columns = ['total_count', 'multimodal_count']
    model_multimodal['multimodal_percentage'] = (model_multimodal['multimodal_count'] / model_multimodal['total_count'] * 100).round(2)
    model_multimodal = model_multimodal.sort_values('multimodal_percentage', ascending=False)
    
    print("实际的前10名模型架构多模态支持:")
    print(model_multimodal[['total_count', 'multimodal_count', 'multimodal_percentage']].head(10))
    print()
    
    print("HTML报告声称的前3名:")
    print("- CodeT5+: 100.00%")
    print("- GPT-4o: 100.00%")
    print("- DALL-E-3: 100.00%")
    print()
    
    # Check specific models mentioned in HTML
    print("检查HTML报告中提到的具体模型架构:")
    for model in ['CodeT5+', 'GPT-4o', 'DALL-E-3']:
        if model in model_multimodal.index:
            row = model_multimodal.loc[model]
            print(f"- {model}: {row['multimodal_percentage']:.2f}% (实际数据)")
        else:
            print(f"- {model}: 未在数据中找到")
    print()
    
    # Question 3: Task Categories by Bias Detection Score
    print("3. 各任务类型偏见检测中位数Top 3")
    print("=" * 60)
    
    # Calculate median bias detection score by task category
    task_bias = df.groupby('task_category')['bias_detection_score'].agg(['median', 'mean', 'count']).round(5)
    task_bias = task_bias.sort_values('median', ascending=False)
    
    print("实际的所有任务类型偏见检测分数中位数:")
    print(task_bias)
    print()
    
    print("HTML报告声称的前3名:")
    print("- Communication: 0.82865")
    print("- Learning & Adaptation: 0.8279")
    print("- Planning & Scheduling: 0.8271")
    print()
    
    # Check specific task categories mentioned in HTML
    print("检查HTML报告中提到的具体任务类型:")
    for task in ['Communication', 'Learning & Adaptation', 'Planning & Scheduling']:
        if task in task_bias.index:
            median_score = task_bias.loc[task, 'median']
            print(f"- {task}: {median_score:.5f} (实际数据)")
        else:
            print(f"- {task}: 未在数据中找到")
    print()
    
    return {
        'agent_multimodal': agent_multimodal,
        'model_multimodal': model_multimodal,
        'task_bias': task_bias,
        'total_records': len(df)
    }

if __name__ == "__main__":
    results = analyze_csv_data_detailed() 