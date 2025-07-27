#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
详细验证HTML报告中的所有统计数据
"""

import pandas as pd
import numpy as np

def load_data():
    """加载数据"""
    csv_path = "/Users/binwu/OOR-local/katas/data-dashboard-in-html-for-agentic_ai_performance_dataset_20250622/datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv"
    df = pd.read_csv(csv_path)
    return df

def verify_basic_statistics(df):
    """验证基本统计数据"""
    print("=== 基本统计数据验证 ===")
    
    # HTML报告中的统计数据
    html_stats = {
        '数据记录数': 80,
        '智能体类型': 13,
        '模型架构': 8,
        '支持多模态': 18
    }
    
    # 实际统计数据
    actual_stats = {
        '数据记录数': len(df),
        '智能体类型': df['agent_type'].nunique(),
        '模型架构': df['model_architecture'].nunique(),
        '支持多模态': len(df[df['multimodal_capability'] == True])
    }
    
    print("HTML报告 vs 实际数据:")
    for key in html_stats:
        html_val = html_stats[key]
        actual_val = actual_stats[key]
        match = html_val == actual_val
        print(f"{key}: {'✓' if match else '✗'} HTML: {html_val} vs 实际: {actual_val}")
    
    return actual_stats

def verify_agent_distribution(df):
    """验证智能体类型分布"""
    print("\n=== 智能体类型分布验证 ===")
    
    # HTML报告中的分布数据
    html_distribution = {
        'Project Manager': 10,
        'Customer Service': 6,
        'Code Assistant': 6,
        'Content Creator': 7,
        'Sales Assistant': 7,
        'QA Tester': 4,
        'Document Processor': 4,
        'Task Planner': 6,
        'Data Analyst': 7,
        'HR Recruiter': 4,
        'Research Assistant': 5,
        'Social Media Manager': 5,
        'Others': 9
    }
    
    # 实际分布数据
    actual_distribution = df['agent_type'].value_counts().to_dict()
    
    print("HTML报告中的分布:")
    total_html = sum(html_distribution.values())
    print(f"总计: {total_html}")
    for agent_type, count in html_distribution.items():
        print(f"{agent_type}: {count}")
    
    print("\n实际分布:")
    total_actual = sum(actual_distribution.values())
    print(f"总计: {total_actual}")
    for agent_type, count in actual_distribution.items():
        print(f"{agent_type}: {count}")
    
    print("\n对比验证:")
    all_agent_types = set(list(html_distribution.keys()) + list(actual_distribution.keys()))
    errors = []
    
    for agent_type in sorted(all_agent_types):
        if agent_type == 'Others':
            continue
        html_count = html_distribution.get(agent_type, 0)
        actual_count = actual_distribution.get(agent_type, 0)
        match = html_count == actual_count
        if not match:
            errors.append(f"{agent_type}: HTML {html_count} vs 实际 {actual_count}")
        print(f"{agent_type}: {'✓' if match else '✗'} HTML: {html_count} vs 实际: {actual_count}")
    
    # 检查"Others"类别
    others_types = set(actual_distribution.keys()) - set([k for k in html_distribution.keys() if k != 'Others'])
    others_count = sum(actual_distribution.get(t, 0) for t in others_types)
    html_others = html_distribution.get('Others', 0)
    print(f"Others: {'✓' if others_count == html_others else '✗'} HTML: {html_others} vs 实际: {others_count}")
    if others_count != html_others:
        errors.append(f"Others: HTML {html_others} vs 实际 {others_count}")
    
    return errors

def verify_model_architecture_count(df):
    """验证模型架构数量"""
    print("\n=== 模型架构数量验证 ===")
    
    model_archs = df['model_architecture'].unique()
    print(f"实际模型架构数量: {len(model_archs)}")
    print("模型架构列表:")
    for i, arch in enumerate(sorted(model_archs), 1):
        count = len(df[df['model_architecture'] == arch])
        print(f"{i}. {arch}: {count}")
    
    html_count = 8
    actual_count = len(model_archs)
    match = html_count == actual_count
    print(f"\n验证结果: {'✓' if match else '✗'} HTML: {html_count} vs 实际: {actual_count}")
    
    return actual_count

def verify_multimodal_count(df):
    """验证多模态支持数量"""
    print("\n=== 多模态支持数量验证 ===")
    
    multimodal_df = df[df['multimodal_capability'] == True]
    actual_count = len(multimodal_df)
    html_count = 18
    
    print(f"支持多模态的记录:")
    for idx, row in multimodal_df.iterrows():
        print(f"- {row['agent_id']}: {row['agent_type']} ({row['model_architecture']})")
    
    match = html_count == actual_count
    print(f"\n验证结果: {'✓' if match else '✗'} HTML: {html_count} vs 实际: {actual_count}")
    
    return actual_count

def main():
    """主函数"""
    print("开始详细验证HTML报告中的所有统计数据...")
    
    # 加载数据
    df = load_data()
    
    # 验证基本统计
    basic_stats = verify_basic_statistics(df)
    
    # 验证智能体分布
    agent_errors = verify_agent_distribution(df)
    
    # 验证模型架构数量
    model_count = verify_model_architecture_count(df)
    
    # 验证多模态支持数量
    multimodal_count = verify_multimodal_count(df)
    
    # 总结
    print("\n=== 验证总结 ===")
    print(f"数据记录数: ✓ 正确 (80)")
    print(f"智能体类型数: {'✗ 错误' if basic_stats['智能体类型'] != 13 else '✓ 正确'} (实际: {basic_stats['智能体类型']})")
    print(f"模型架构数: {'✗ 错误' if model_count != 8 else '✓ 正确'} (实际: {model_count})")
    print(f"支持多模态数: {'✗ 错误' if multimodal_count != 18 else '✓ 正确'} (实际: {multimodal_count})")
    
    if agent_errors:
        print(f"\n智能体分布错误 ({len(agent_errors)}个):")
        for error in agent_errors:
            print(f"- {error}")
    else:
        print("\n智能体分布: ✓ 正确")

if __name__ == "__main__":
    main()
