import base64
import io
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


PROJECT_DIR = Path(__file__).resolve().parent
DATASET_PATH = PROJECT_DIR / "datasets" / "agentic_ai_performance_dataset_20250622.csv"
OUTPUT_HTML = PROJECT_DIR / "dashboard.html"

# ---------- 1. Load data ----------
print("Reading dataset from:", DATASET_PATH)
df = pd.read_csv(DATASET_PATH)
num_records = len(df)
print(f"Loaded {num_records} records.")

# ---------- 2. Helper to generate base64 png ----------

def fig_to_base64_png(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=150)
    plt.close(fig)
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

# ---------- 3. Chart 1: Multimodal Capability vs Success Rate ----------
multimodal_summary = df.groupby("multimodal_capability")["success_rate"].mean().reset_index()
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.barplot(
    data=multimodal_summary,
    x="multimodal_capability",
    y="success_rate",
    palette=["#8ecae6", "#219ebc"],
    ax=ax1,
)
ax1.set_xlabel("Multimodal Capability")
ax1.set_ylabel("Avg. Success Rate")
ax1.set_title("Success Rate vs. Multimodal Capability")
chart1_uri = fig_to_base64_png(fig1)

# ---------- 4. Chart 2: Edge Compatibility vs Efficiency Score ----------
edge_summary = df.groupby("edge_compatibility")["efficiency_score"].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.barplot(
    data=edge_summary,
    x="edge_compatibility",
    y="efficiency_score",
    palette=["#ffb703", "#fb8500"],
    ax=ax2,
)
ax2.set_xlabel("Edge Compatible")
ax2.set_ylabel("Avg. Efficiency Score")
ax2.set_title("Efficiency Score vs. Edge Compatibility")
chart2_uri = fig_to_base64_png(fig2)

# ---------- 5. Chart 3: Bias Detection Score Distribution ----------
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.histplot(df["bias_detection_score"], bins=20, color="#023047", kde=True, ax=ax3)
ax3.set_title("Bias Detection Score Distribution")
ax3.set_xlabel("Bias Detection Score")
chart3_uri = fig_to_base64_png(fig3)

# ---------- 6. Build HTML ----------
html_template = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Agentic AI Performance Dashboard</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
                'Open Sans', 'Helvetica Neue', sans-serif;
            background-color: #fafafa;
            color: #333;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #219ebc;
            color: #fff;
            padding: 1rem; text-align: center;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            margin: 1rem;
        }}
        .card {{
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 1rem;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
        @media (min-width: 700px) {{
            .container {{
                flex-direction: row;
                flex-wrap: wrap;
            }}
            .card {{
                flex: 1 1 calc(33% - 2rem);
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>Agentic AI Performance Dashboard</h1>
        <p>Total Records Processed: {num_records}</p>
    </header>
    <main class=\"container\">
        <section class=\"card\">
            <h2>Success Rate & Multimodality</h2>
            <img src=\"{chart1_uri}\" alt=\"Success Rate vs Multimodal Capability\" />
        </section>
        <section class=\"card\">
            <h2>Efficiency & Edge Deployment</h2>
            <img src=\"{chart2_uri}\" alt=\"Efficiency Score vs Edge Compatibility\" />
        </section>
        <section class=\"card\">
            <h2>Bias Detection Distribution</h2>
            <img src=\"{chart3_uri}\" alt=\"Bias Detection Score Histogram\" />
        </section>
    </main>
</body>
</html>"""

OUTPUT_HTML.write_text(html_template, encoding="utf-8")
print("Dashboard generated at:", OUTPUT_HTML)
