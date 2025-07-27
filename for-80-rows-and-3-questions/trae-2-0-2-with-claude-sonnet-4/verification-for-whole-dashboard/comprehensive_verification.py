#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面验证HTML报告中的所有分析结果
"""

import pandas as pd
import numpy as np
from collections import Counter
import json

def load_data():
    """加载数据"""
    csv_path = "/Users/binwu/OOR-local/katas/data-dashboard-in-html-for-agentic_ai_performance_dataset_20250622/datasets/first-80-rows-agentic_ai_performance_dataset_20250622.csv"
    df = pd.read_csv(csv_path)
    print(f"数据集总行数: {len(df)}")
    return df

def verify_question_1(df):
    """验证问题1：支持多模态的智能体类型占比TOP3"""
    print("\n=== 问题1验证：支持多模态的智能体类型占比TOP3 ===")
    
    # 获取支持多模态的数据
    multimodal_df = df[df['multimodal_capability'] == True]
    print(f"支持多模态的记录数: {len(multimodal_df)}")
    
    # 统计各智能体类型的总数和支持多模态的数量
    agent_type_total = df['agent_type'].value_counts()
    agent_type_multimodal = multimodal_df['agent_type'].value_counts()
    
    # 计算占比
    agent_type_ratio = {}
    for agent_type in agent_type_total.index:
        total_count = agent_type_total[agent_type]
        multimodal_count = agent_type_multimodal.get(agent_type, 0)
        ratio = (multimodal_count / total_count) * 100
        agent_type_ratio[agent_type] = {
            'total': total_count,
            'multimodal': multimodal_count,
            'ratio': ratio
        }
    
    # 按占比排序
    sorted_ratios = sorted(agent_type_ratio.items(), key=lambda x: x[1]['ratio'], reverse=True)
    
    print("所有智能体类型的多模态支持占比:")
    for i, (agent_type, data) in enumerate(sorted_ratios, 1):
        print(f"{i}. {agent_type}: {data['multimodal']}/{data['total']} = {data['ratio']:.2f}%")
    
    print("\nTOP3结果:")
    top3 = sorted_ratios[:3]
    for i, (agent_type, data) in enumerate(top3, 1):
        print(f"{i}. {agent_type}: {data['ratio']:.2f}%")
    
    # HTML报告中的结果
    html_results = [
        ('Code Assistant', 66.67),
        ('Document Processor', 50.00),
        ('Content Creator', 42.86)
    ]
    
    print("\nHTML报告中的结果:")
    for i, (agent_type, ratio) in enumerate(html_results, 1):
        print(f"{i}. {agent_type}: {ratio}%")
    
    print("\n验证结果:")
    correct_top3 = [(agent_type, data['ratio']) for agent_type, data in top3]
    for i, ((correct_type, correct_ratio), (html_type, html_ratio)) in enumerate(zip(correct_top3, html_results), 1):
        match = correct_type == html_type and abs(correct_ratio - html_ratio) < 0.01
        print(f"第{i}名: {'✓' if match else '✗'} 正确: {correct_type} {correct_ratio:.2f}% vs HTML: {html_type} {html_ratio}%")
    
    return correct_top3

def verify_question_2(df):
    """验证问题2：支持多模态的模型架构占比TOP3"""
    print("\n=== 问题2验证：支持多模态的模型架构占比TOP3 ===")
    
    # 获取支持多模态的数据
    multimodal_df = df[df['multimodal_capability'] == True]
    
    # 统计各模型架构的总数和支持多模态的数量
    model_arch_total = df['model_architecture'].value_counts()
    model_arch_multimodal = multimodal_df['model_architecture'].value_counts()
    
    # 计算占比
    model_arch_ratio = {}
    for model_arch in model_arch_total.index:
        total_count = model_arch_total[model_arch]
        multimodal_count = model_arch_multimodal.get(model_arch, 0)
        ratio = (multimodal_count / total_count) * 100
        model_arch_ratio[model_arch] = {
            'total': total_count,
            'multimodal': multimodal_count,
            'ratio': ratio
        }
    
    # 按占比排序
    sorted_ratios = sorted(model_arch_ratio.items(), key=lambda x: x[1]['ratio'], reverse=True)
    
    print("所有模型架构的多模态支持占比:")
    for i, (model_arch, data) in enumerate(sorted_ratios, 1):
        print(f"{i}. {model_arch}: {data['multimodal']}/{data['total']} = {data['ratio']:.2f}%")
    
    print("\nTOP3结果:")
    top3 = sorted_ratios[:3]
    for i, (model_arch, data) in enumerate(top3, 1):
        print(f"{i}. {model_arch}: {data['ratio']:.2f}%")
    
    # HTML报告中的结果
    html_results = [
        ('CodeT5+', 50.00),
        ('GPT-4o', 37.50),
        ('Transformer-XL', 22.22)
    ]
    
    print("\nHTML报告中的结果:")
    for i, (model_arch, ratio) in enumerate(html_results, 1):
        print(f"{i}. {model_arch}: {ratio}%")
    
    print("\n验证结果:")
    correct_top3 = [(model_arch, data['ratio']) for model_arch, data in top3]
    for i, ((correct_arch, correct_ratio), (html_arch, html_ratio)) in enumerate(zip(correct_top3, html_results), 1):
        match = correct_arch == html_arch and abs(correct_ratio - html_ratio) < 0.01
        print(f"第{i}名: {'✓' if match else '✗'} 正确: {correct_arch} {correct_ratio:.2f}% vs HTML: {html_arch} {html_ratio}%")
    
    return correct_top3

def verify_question_3(df):
    """验证问题3：各任务类型bias detection中位数TOP3"""
    print("\n=== 问题3验证：各任务类型bias detection中位数TOP3 ===")
    
    # 按任务类型分组，计算bias_detection_score的中位数
    task_bias_median = df.groupby('task_category')['bias_detection_score'].median().sort_values(ascending=False)
    
    print("所有任务类型的bias detection中位数:")
    for i, (task_category, median_score) in enumerate(task_bias_median.items(), 1):
        print(f"{i}. {task_category}: {median_score:.4f}")
    
    print("\nTOP3结果:")
    top3 = list(task_bias_median.head(3).items())
    for i, (task_category, median_score) in enumerate(top3, 1):
        print(f"{i}. {task_category}: {median_score:.4f}")
    
    # HTML报告中的结果
    html_results = [
        ('Communication', 0.8061),
        ('Planning & Scheduling', 0.7657),
        ('Text Processing', 0.7463)
    ]
    
    print("\nHTML报告中的结果:")
    for i, (task_category, median_score) in enumerate(html_results, 1):
        print(f"{i}. {task_category}: {median_score}")
    
    print("\n验证结果:")
    for i, ((correct_task, correct_median), (html_task, html_median)) in enumerate(zip(top3, html_results), 1):
        match = correct_task == html_task and abs(correct_median - html_median) < 0.001
        print(f"第{i}名: {'✓' if match else '✗'} 正确: {correct_task} {correct_median:.4f} vs HTML: {html_task} {html_median}")
    
    return top3

def verify_other_statistics(df):
    """验证其他统计数据"""
    print("\n=== 其他统计数据验证 ===")
    
    # 基本统计
    total_records = len(df)
    multimodal_count = len(df[df['multimodal_capability'] == True])
    edge_compatible_count = len(df[df['edge_compatibility'] == True])
    
    print(f"数据集总记录数: {total_records}")
    print(f"支持多模态的记录数: {multimodal_count}")
    print(f"支持边缘计算的记录数: {edge_compatible_count}")
    
    # 智能体类型分布
    print("\n智能体类型分布:")
    agent_type_dist = df['agent_type'].value_counts()
    for agent_type, count in agent_type_dist.items():
        print(f"{agent_type}: {count}")
    
    # 模型架构分布
    print("\n模型架构分布:")
    model_arch_dist = df['model_architecture'].value_counts()
    for model_arch, count in model_arch_dist.items():
        print(f"{model_arch}: {count}")
    
    # 任务类型分布
    print("\n任务类型分布:")
    task_category_dist = df['task_category'].value_counts()
    for task_category, count in task_category_dist.items():
        print(f"{task_category}: {count}")
    
    # 部署环境分布
    print("\n部署环境分布:")
    deployment_env_dist = df['deployment_environment'].value_counts()
    for env, count in deployment_env_dist.items():
        print(f"{env}: {count}")
    
    # 性能指标统计
    print("\n性能指标统计:")
    performance_metrics = ['success_rate', 'accuracy_score', 'efficiency_score', 'bias_detection_score']
    for metric in performance_metrics:
        mean_val = df[metric].mean()
        median_val = df[metric].median()
        std_val = df[metric].std()
        print(f"{metric}: 均值={mean_val:.4f}, 中位数={median_val:.4f}, 标准差={std_val:.4f}")
    
    return {
        'total_records': total_records,
        'multimodal_count': multimodal_count,
        'edge_compatible_count': edge_compatible_count,
        'agent_type_dist': agent_type_dist.to_dict(),
        'model_arch_dist': model_arch_dist.to_dict(),
        'task_category_dist': task_category_dist.to_dict(),
        'deployment_env_dist': deployment_env_dist.to_dict()
    }

def main():
    """主函数"""
    print("开始全面验证HTML报告中的分析结果...")
    
    # 加载数据
    df = load_data()
    
    # 验证三个核心问题
    q1_results = verify_question_1(df)
    q2_results = verify_question_2(df)
    q3_results = verify_question_3(df)
    
    # 验证其他统计数据
    other_stats = verify_other_statistics(df)
    
    # 生成验证报告
    verification_report = {
        'data_summary': {
            'total_records': len(df),
            'columns': list(df.columns),
            'data_types': df.dtypes.to_dict()
        },
        'question_1': {
            'correct_results': q1_results,
            'html_results': [('Code Assistant', 66.67), ('Document Processor', 50.00), ('Content Creator', 42.86)]
        },
        'question_2': {
            'correct_results': q2_results,
            'html_results': [('CodeT5+', 50.00), ('GPT-4o', 37.50), ('Transformer-XL', 22.22)]
        },
        'question_3': {
            'correct_results': q3_results,
            'html_results': [('Communication', 0.8061), ('Planning & Scheduling', 0.7657), ('Text Processing', 0.7463)]
        },
        'other_statistics': other_stats
    }
    
    # 保存验证报告
    report_path = "/Users/binwu/OOR-local/katas/data-dashboard-in-html-for-agentic_ai_performance_dataset_20250622/for-80-rows-and-3-questions/verification_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(verification_report, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n验证报告已保存到: {report_path}")
    print("\n验证完成！")

if __name__ == "__main__":
    main()
