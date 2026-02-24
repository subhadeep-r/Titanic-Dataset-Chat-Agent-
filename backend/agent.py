from typing import Optional, Tuple, Dict
import pandas as pd
import seaborn as sns
import matplotlib
# Use non-interactive backend for environments without a display (tests, CI)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64


def _img_to_base64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


class TitanicAgent:

    def __init__(self, df: Optional[pd.DataFrame] = None):
        if df is None:
            self.df = sns.load_dataset("titanic")
        else:
            self.df = df.copy()

    def ask(self, question: str) -> Dict[str, Optional[str]]:
        q = question.lower().strip()

        if ("percentage" in q or "percent" in q) and "male" in q:
            total = len(self.df)
            males = int((self.df["sex"] == "male").sum())
            pct = males / total * 100 if total else 0
            return {"answer": f"{pct:.1f}% of passengers were male ({males}/{total}).", "image": None}

        if ("histogram" in q or "distribution" in q) and "age" in q:
            ages = self.df["age"].dropna()
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(ages, bins=20, color="#1f77b4", edgecolor="black")
            ax.set_xlabel("Age")
            ax.set_ylabel("Count")
            ax.set_title("Distribution of Passenger Ages")
            img = _img_to_base64(fig)
            return {"answer": f"Histogram of passenger ages (n={len(ages)}).", "image": img}

        if ("average" in q or "mean" in q) and ("fare" in q or "ticket fare" in q):
            fares = self.df["fare"].dropna()
            mean_fare = fares.mean()
            return {"answer": f"Average ticket fare: ${mean_fare:.2f} (n={len(fares)}).", "image": None}

        if ("embark" in q) or ("embarked from" in q) or ("port" in q):
            counts = self.df["embarked"].value_counts(dropna=False)
            lines = []
            for port, c in counts.items():
                port_label = str(port) if pd.notna(port) else "(missing)"
                lines.append(f"{port_label}: {c}")
            fig, ax = plt.subplots(figsize=(5, 3))
            counts.plot(kind="bar", ax=ax, color="#2ca02c")
            ax.set_xlabel("Embarkation Port")
            ax.set_ylabel("Passengers")
            ax.set_title("Passengers by Embarkation Port")
            img = _img_to_base64(fig)
            return {"answer": "\n".join(lines), "image": img}

        if ("how many" in q or "number of passengers" in q or "count" in q) and ("passeng" in q or "passengers" in q):
            total = len(self.df)
            return {"answer": f"There were {total} passengers in the dataset.", "image": None}

        for col in ["age", "fare", "sibsp", "parch"]:
            if col in q:
                series = self.df[col].dropna()
                if "average" in q or "mean" in q:
                    return {"answer": f"Mean {col}: {series.mean():.2f} (n={len(series)}).", "image": None}
                if "median" in q:
                    return {"answer": f"Median {col}: {series.median():.2f} (n={len(series)}).", "image": None}

        cols = ", ".join(self.df.columns.tolist())
        return {"answer": f"I couldn't detect a specific metric from your question. Dataset has columns: {cols}", "image": None}
