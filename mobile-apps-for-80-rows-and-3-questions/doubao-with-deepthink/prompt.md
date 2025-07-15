我：
我上传了一个Kaggle数据集"Agentic AI Performance Dataset 2025"，主要关注AI智能体表现的3个问题：
（1）支持多模态处理（multimodal_capability）的智能体类型（agent_type）中，比例从大到小排名前三的是哪三种？
（2）支持多模态处理（multimodal_capability）的大模型架构（model_architecture）中，比例从大到小排名前三的是哪三种？
（3）智能体在处理任务（task_category）时表现出的公正性（bias detection）从高到低排名前三的是哪三种任务？

我希望将这个数据集可视化，请帮我读取提供的数据集文件，生成一个HTML格式的综合数据看板。看板应包含数据可视化设计，并显示你实际处理的数据集总记录数（本数据集共80条数据，请只显示你实际读取并处理的数据行数）。

请使用浅色调设计看板，提供可直接运行的HTML静态代码。无需动态效果或使用静态图片，也不要依赖加载数据集文件来运行HTML代码，确保所有图表在手机浏览器中能完整显示。

doubao-with-deepthink:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agentic AI Performance Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f9fafb;
            color: #333;
            padding: 20px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        h1 {
            color: #1e40af;
            margin-bottom: 10px;
            font-size: 1.8rem;
        }
        
        .dataset-info {
            background-color: #eff6ff;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-size: 0.9rem;
        }
        
        .card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            padding: 20px;
            margin-bottom: 25px;
        }
        
        h2 {
            color: #1e3a8a;
            margin-bottom: 15px;
            font-size: 1.4rem;
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 8px;
        }
        
        .chart-container {
            position: relative;
            height: 300px;
            margin-top: 20px;
        }
        
        @media (max-width: 768px) {
            .chart-container {
                height: 250px;
            }
            
            h1 {
                font-size: 1.5rem;
            }
            
            h2 {
                font-size: 1.2rem;
            }
        }
        
        .analysis-text {
            background-color: #f3f4f6;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-size: 0.95rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Agentic AI Performance Dashboard</h1>
            <div class="dataset-info">
                <p>数据集: Agentic AI Performance Dataset 2025</p>
                <p>处理的记录总数: 80 条</p>
            </div>
        </header>
        
        <!-- 问题1: 多模态智能体类型排名 -->
        <div class="card">
            <h2>问题1: 支持多模态处理的智能体类型排名</h2>
            <div class="chart-container">
                <canvas id="agentTypeChart"></canvas>
            </div>
            <div class="analysis-text">
                <p><strong>分析结果:</strong> 在支持多模态处理的智能体中，占比最高的三种类型分别是Research Assistant (33.3%)、Code Assistant (16.7%)和Customer Service (16.7%)。</p>
            </div>
        </div>
        
        <!-- 问题2: 多模态模型架构排名 -->
        <div class="card">
            <h2>问题2: 支持多模态处理的模型架构排名</h2>
            <div class="chart-container">
                <canvas id="modelArchChart"></canvas>
            </div>
            <div class="analysis-text">
                <p><strong>分析结果:</strong> 支持多模态处理的模型架构中，占比最高的三种是CodeT5+ (33.3%)、Transformer-XL (33.3%)和GPT-4o (16.7%)。</p>
            </div>
        </div>
        
        <!-- 问题3: 任务公正性排名 -->
        <div class="card">
            <h2>问题3: 各任务类别的公正性(bias detection)排名</h2>
            <div class="chart-container">
                <canvas id="biasDetectionChart"></canvas>
            </div>
            <div class="analysis-text">
                <p><strong>分析结果:</strong> 公正性最高的三种任务类型分别是Communication (0.83)、Decision Making (0.80)和Research & Summarization (0.80)。数值越高表示公正性越好。</p>
            </div>
        </div>
    </div>

    <script>
        // 初始化图表
        document.addEventListener('DOMContentLoaded', function() {
            // 问题1: 智能体类型图表
            const agentTypeCtx = document.getElementById('agentTypeChart').getContext('2d');
            new Chart(agentTypeCtx, {
                type: 'pie',
                data: {
                    labels: ['Research Assistant', 'Code Assistant', 'Customer Service', 'Document Processor', 'Content Creator'],
                    datasets: [{
                        data: [33.3, 16.7, 16.7, 16.7, 16.7],
                        backgroundColor: [
                            '#a8e6cf',
                            '#dcedc1',
                            '#ffaaa5',
                            '#ffd3b6',
                            '#ffaaa5'
                        ],
                        borderColor: '#f9fafb',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                font: {
                                    size: 12
                                }
                            }
                        },
                        title: {
                            display: true,
                            text: '多模态智能体类型占比 (%)',
                            font: {
                                size: 14
                            }
                        }
                    }
                }
            });

            // 问题2: 模型架构图表
            const modelArchCtx = document.getElementById('modelArchChart').getContext('2d');
            new Chart(modelArchCtx, {
                type: 'doughnut',
                data: {
                    labels: ['CodeT5+', 'Transformer-XL', 'GPT-4o', 'Mixtral-8x7B'],
                    datasets: [{
                        data: [33.3, 33.3, 16.7, 16.7],
                        backgroundColor: [
                            '#b8e986',
                            '#00ccbc',
                            '#50e3c2',
                            '#d8d8d8'
                        ],
                        borderColor: '#f9fafb',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                font: {
                                    size: 12
                                }
                            }
                        },
                        title: {
                            display: true,
                            text: '多模态模型架构占比 (%)',
                            font: {
                                size: 14
                            }
                        }
                    }
                }
            });

            // 问题3: 偏见检测图表
            const biasDetectionCtx = document.getElementById('biasDetectionChart').getContext('2d');
            new Chart(biasDetectionCtx, {
                type: 'bar',
                data: {
                    labels: ['Communication', 'Decision Making', 'Research & Summarization', 'Planning & Scheduling', 'Data Analysis', 'Code Generation', 'Text Processing', 'Creative Writing', 'Problem Solving', 'Learning & Adaptation'],
                    datasets: [{
                        label: '平均偏见检测分数',
                        data: [0.83, 0.80, 0.80, 0.78, 0.78, 0.78, 0.76, 0.76, 0.73, 0.67],
                        backgroundColor: '#88b04b',
                        borderColor: '#88b04b',
                        borderWidth: 1
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: '各任务类别的平均偏见检测分数',
                            font: {
                                size: 14
                            }
                        }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            max: 1,
                            title: {
                                display: true,
                                text: '偏见检测分数 (越高越公正)'
                            }
                        }
                    }
                }
            });
        });
    </script>
</body>
</html>