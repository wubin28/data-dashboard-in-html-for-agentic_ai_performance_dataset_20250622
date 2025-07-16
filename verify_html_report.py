import pandas as pd
import numpy as np

def analyze_csv_data():
    # Read the CSV file
    df = pd.read_csv('datasets/agentic_ai_performance_dataset_20250622.csv')
    
    print("=== CSV Data Analysis and HTML Report Verification ===")
    print(f"Total records: {len(df)}")
    print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
    print()
    
    # Question 1: Agent Types with Highest Multimodal Capability
    print("1. AGENT TYPES WITH HIGHEST MULTIMODAL CAPABILITY")
    print("=" * 60)
    
    # Calculate multimodal capability percentage by agent type
    agent_multimodal = df.groupby('agent_type').agg({
        'multimodal_capability': ['count', 'sum']
    }).round(4)
    agent_multimodal.columns = ['total_count', 'multimodal_count']
    agent_multimodal['multimodal_percentage'] = (agent_multimodal['multimodal_count'] / agent_multimodal['total_count'] * 100).round(2)
    agent_multimodal = agent_multimodal.sort_values('multimodal_percentage', ascending=False)
    
    print("Top 15 Agent Types by Multimodal Capability:")
    print(agent_multimodal[['multimodal_percentage']].head(15))
    print()
    
    print("HTML Report Claims (Top 3):")
    print("- Translation Agent: 22.4%")
    print("- Content Creator: 21.8%") 
    print("- Document Processor: 20.5%")
    print()
    
    # Question 2: Model Architectures with Highest Multimodal Support
    print("2. MODEL ARCHITECTURES WITH HIGHEST MULTIMODAL SUPPORT")
    print("=" * 60)
    
    # Calculate multimodal capability percentage by model architecture
    model_multimodal = df.groupby('model_architecture').agg({
        'multimodal_capability': ['count', 'sum']
    }).round(4)
    model_multimodal.columns = ['total_count', 'multimodal_count']
    model_multimodal['multimodal_percentage'] = (model_multimodal['multimodal_count'] / model_multimodal['total_count'] * 100).round(2)
    model_multimodal = model_multimodal.sort_values('multimodal_percentage', ascending=False)
    
    print("Top 10 Model Architectures by Multimodal Support:")
    print(model_multimodal[['multimodal_percentage']].head(10))
    print()
    
    print("HTML Report Claims (Top 3):")
    print("- Claude-3.5: 24.6%")
    print("- Gemini-Pro: 22.1%")
    print("- GPT-4o: 20.8%")
    print()
    
    # Question 3: Task Categories by Bias Detection Score
    print("3. TASK CATEGORIES BY BIAS DETECTION SCORE")
    print("=" * 60)
    
    # Calculate median bias detection score by task category
    task_bias = df.groupby('task_category')['bias_detection_score'].agg(['median', 'mean', 'count']).round(4)
    task_bias = task_bias.sort_values('median', ascending=False)
    
    print("All Task Categories by Median Bias Detection Score:")
    print(task_bias)
    print()
    
    print("HTML Report Claims (Top 3 by median):")
    print("- Decision Making: 0.87")
    print("- Creative Writing: 0.84")
    print("- Communication: 0.83")
    print()
    
    return {
        'agent_multimodal': agent_multimodal,
        'model_multimodal': model_multimodal,
        'task_bias': task_bias,
        'total_records': len(df)
    }

if __name__ == "__main__":
    results = analyze_csv_data() 