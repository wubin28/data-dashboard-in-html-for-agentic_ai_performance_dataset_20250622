#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证HTML报告中的分析结果是否与Excel原始数据相符
"""

import pandas as pd
import numpy as np
from collections import Counter

def load_data():
    """加载CSV数据"""
    file_path = "/Users/binwu/OOR-local/katas/data-dashboard-in-html-for-agentic_ai_performance_dataset_20250622/datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv"
    df = pd.read_csv(file_path)
    print(f"数据加载完成，共 {len(df)} 条记录")
    return df

def analyze_question_1(df):
    """
    问题1：支持多模态处理（multimodal_capability）的智能体类型（agent_type）
    在该智能体类型中的占比从大到小排名前三的智能体类型是哪三个？
    """
    print("\n=== 问题1分析：支持多模态的智能体类型占比TOP3 ===")
    
    # 统计每种智能体类型的总数和支持多模态的数量
    agent_stats = {}
    
    for agent_type in df['agent_type'].unique():
        agent_data = df[df['agent_type'] == agent_type]
        total_count = len(agent_data)
        multimodal_count = len(agent_data[agent_data['multimodal_capability'] == True])
        percentage = (multimodal_count / total_count) * 100 if total_count > 0 else 0
        
        agent_stats[agent_type] = {
            'total': total_count,
            'multimodal': multimodal_count,
            'percentage': percentage
        }
    
    # 按占比排序
    sorted_agents = sorted(agent_stats.items(), key=lambda x: x[1]['percentage'], reverse=True)
    
    print("所有智能体类型的多模态支持情况：")
    for i, (agent_type, stats) in enumerate(sorted_agents):
        print(f"{i+1:2d}. {agent_type:<20}: {stats['percentage']:6.2f}% ({stats['multimodal']}/{stats['total']})")
    
    print("\nTOP3结果：")
    for i in range(min(3, len(sorted_agents))):
        agent_type, stats = sorted_agents[i]
        print(f"{i+1}. {agent_type}: {stats['percentage']:.2f}% ({stats['multimodal']}/{stats['total']})")
    
    return sorted_agents[:3]

def analyze_question_2(df):
    """
    问题2：支持多模态处理（multimodal_capability）的大模型架构（model_architecture）
    在该大模型架构中的占比从大到小排名前三的大模型架构是哪三个？
    """
    print("\n=== 问题2分析：支持多模态的大模型架构占比TOP3 ===")
    
    # 统计每种模型架构的总数和支持多模态的数量
    model_stats = {}
    
    for model_arch in df['model_architecture'].unique():
        model_data = df[df['model_architecture'] == model_arch]
        total_count = len(model_data)
        multimodal_count = len(model_data[model_data['multimodal_capability'] == True])
        percentage = (multimodal_count / total_count) * 100 if total_count > 0 else 0
        
        model_stats[model_arch] = {
            'total': total_count,
            'multimodal': multimodal_count,
            'percentage': percentage
        }
    
    # 按占比排序
    sorted_models = sorted(model_stats.items(), key=lambda x: x[1]['percentage'], reverse=True)
    
    print("所有大模型架构的多模态支持情况：")
    for i, (model_arch, stats) in enumerate(sorted_models):
        print(f"{i+1:2d}. {model_arch:<15}: {stats['percentage']:6.2f}% ({stats['multimodal']}/{stats['total']})")
    
    print("\nTOP3结果：")
    for i in range(min(3, len(sorted_models))):
        model_arch, stats = sorted_models[i]
        print(f"{i+1}. {model_arch}: {stats['percentage']:.2f}% ({stats['multimodal']}/{stats['total']})")
    
    return sorted_models[:3]

def analyze_question_3(df):
    """
    问题3：各种智能体处理任务（task_category）各自的智能体表现的公正性（bias detection）
    的中位数从高到低排名前三的是哪三种智能体处理任务？
    """
    print("\n=== 问题3分析：各任务类型bias detection中位数TOP3 ===")
    
    # 统计每种任务类型的bias_detection_score中位数
    task_stats = {}
    
    for task_category in df['task_category'].unique():
        task_data = df[df['task_category'] == task_category]
        bias_scores = task_data['bias_detection_score'].dropna()
        
        if len(bias_scores) > 0:
            median_score = bias_scores.median()
            count = len(bias_scores)
            task_stats[task_category] = {
                'median': median_score,
                'count': count,
                'scores': bias_scores.tolist()
            }
    
    # 按中位数排序
    sorted_tasks = sorted(task_stats.items(), key=lambda x: x[1]['median'], reverse=True)
    
    print("所有任务类型的bias detection中位数：")
    for i, (task_category, stats) in enumerate(sorted_tasks):
        print(f"{i+1:2d}. {task_category:<25}: {stats['median']:.4f} (样本数: {stats['count']})")
    
    print("\nTOP3结果：")
    for i in range(min(3, len(sorted_tasks))):
        task_category, stats = sorted_tasks[i]
        print(f"{i+1}. {task_category}: {stats['median']:.4f}")
    
    return sorted_tasks[:3]

def verify_html_results(df):
    """验证HTML报告中的结果"""
    print("\n" + "="*60)
    print("验证HTML报告中的分析结果")
    print("="*60)
    
    # HTML报告中的结果
    html_q1_results = [
        ("Code Assistant", 66.67, "4/6"),
        ("Document Processor", 50.00, "2/4"),
        ("Content Creator", 42.86, "3/7")
    ]
    
    html_q2_results = [
        ("CodeT5+", 50.00, "4/8"),
        ("GPT-4o", 37.50, "3/8"),
        ("Transformer-XL", 22.22, "2/9")
    ]
    
    html_q3_results = [
        ("Communication", 0.8061),
        ("Planning & Scheduling", 0.7657),
        ("Text Processing", 0.7463)
    ]
    
    # 实际分析结果
    actual_q1 = analyze_question_1(df)
    actual_q2 = analyze_question_2(df)
    actual_q3 = analyze_question_3(df)
    
    print("\n" + "="*60)
    print("结果对比")
    print("="*60)
    
    # 问题1对比
    print("\n问题1对比：")
    print("HTML报告结果 vs 实际计算结果")
    for i in range(3):
        html_name, html_pct, html_ratio = html_q1_results[i]
        actual_name, actual_stats = actual_q1[i]
        actual_pct = actual_stats['percentage']
        actual_ratio = f"{actual_stats['multimodal']}/{actual_stats['total']}"
        
        match = "✓" if html_name == actual_name and abs(html_pct - actual_pct) < 0.1 else "✗"
        print(f"{i+1}. {match} {html_name} {html_pct}% ({html_ratio}) vs {actual_name} {actual_pct:.2f}% ({actual_ratio})")
    
    # 问题2对比
    print("\n问题2对比：")
    print("HTML报告结果 vs 实际计算结果")
    for i in range(3):
        html_name, html_pct, html_ratio = html_q2_results[i]
        actual_name, actual_stats = actual_q2[i]
        actual_pct = actual_stats['percentage']
        actual_ratio = f"{actual_stats['multimodal']}/{actual_stats['total']}"
        
        match = "✓" if html_name == actual_name and abs(html_pct - actual_pct) < 0.1 else "✗"
        print(f"{i+1}. {match} {html_name} {html_pct}% ({html_ratio}) vs {actual_name} {actual_pct:.2f}% ({actual_ratio})")
    
    # 问题3对比
    print("\n问题3对比：")
    print("HTML报告结果 vs 实际计算结果")
    for i in range(3):
        html_name, html_median = html_q3_results[i]
        actual_name, actual_stats = actual_q3[i]
        actual_median = actual_stats['median']
        
        match = "✓" if html_name == actual_name and abs(html_median - actual_median) < 0.001 else "✗"
        print(f"{i+1}. {match} {html_name} {html_median:.4f} vs {actual_name} {actual_median:.4f}")

def main():
    """主函数"""
    print("开始验证HTML报告中的分析结果...")
    
    # 加载数据
    df = load_data()
    
    # 验证结果
    verify_html_results(df)
    
    print("\n验证完成！")

if __name__ == "__main__":
    main()
