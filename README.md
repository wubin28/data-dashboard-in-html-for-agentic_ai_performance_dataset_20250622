# AI辅助Excel数据分析与可视化实战型评测：基于 Kaggle “Agentic AI Performance Dataset 2025” 数据集的主流AI编程工具与大模型搭配组合数据分析与可视化表现

## 项目简介
本项目旨在通过实战方法，基于 Kaggle 数据集 [Agentic AI Performance Dataset 2025](https://www.kaggle.com/datasets/bismasajjad/agentic-ai-performance-and-capabilities-dataset)，系统评测国内外主流 AI 编程工具与搭配大模型组合在 Excel 数据分析及可视化方面的表现。通过对比不同工具和大模型在处理真实数据分析任务时的HTML综合数据看板设计美观度和数据准确性，为AI辅助Excel数据分析与可视化实际应用提供参考。

## 目录结构与主要文件说明

- `datasets/`  
  存放原始数据集及其子集：
  - `agentic_ai_performance_dataset_20250622.csv` / `.xlsx`：完整数据集。
  - `first-80-rows-agentic_ai_performance_dataset_20250622.csv` / `.xlsx`：前80行子集，便于快速实验和对比。

- `for-5000-rows-and-3-questions/`  
  针对完整5000行数据集和3个典型分析问题的实战记录。每个子文件夹对应一种AI工具+大模型组合：
  - 如 `windsurf-with-gemini-2.5-pro/`、`cursor-with-o3/` 等，内含：
    - `data-dashboard-by-*.html`：该组合生成的可视化仪表盘页面。
    - `prompt.md`：任务提示词及操作记录。
    - `verification/`：结果验证材料，包括 `verification.md`（人工或自动校验说明）、`verify_html_report_2.py`（自动校验脚本）。

- `for-80-rows-and-3-questions/`  
  针对80行子集和3个问题的快速实验，结构同上。便于不同工具/模型组合下的小规模对比。

- `vague-prompts/`  
  针对模糊/不明确提示词的实验，探索不同AI工具对开放性任务的理解和表现。包含：
  - `ai-ides-for-5000-rows/`、`mobile-apps-for-5000-rows/` 等，进一步细分到具体工具和模型。
  - 各子目录下通常包含对应的 `data-dashboard-by-*.html` 可视化页面。

## 其他说明
- 本项目推荐在国内外主流AI编程环境下复现，便于横向对比。
- 欢迎补充更多工具/模型组合的实验结果。

## 相关文章

- [Kimi搭配K2大模型竟然编造HTML看板数据](https://xiaowuaibikengpu.com/kimi-with-k2-llm-unexpectedly-fabricates-data-in-html-dashboard/)
- [咋用Kimi搭配K2大模型生成HTML炫酷数据看板](https://xiaowuaibikengpu.com/how-to-use-kimi-with-k2-to-generate-html-data-dashboard/)
- [咋用Windsurf搭配Claude Sonnet 4修正HTML看板数据](https://xiaowuaibikengpu.com/how-to-use-windsurf-with-claude-sonnet-4-to-fix-error-data-in-html-dashboard/)
