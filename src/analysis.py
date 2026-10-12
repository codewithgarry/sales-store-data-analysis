"""Exploratory data analysis of the Sales Store product dataset.

Loads data/sales_store.csv, prints summary statistics and saves charts to images/.

Usage:
    python src/analysis.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sales_store.csv"
OUT = ROOT / "images"

sns.set_theme(style="whitegrid", palette="deep")


def save(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", dpi=120)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(DATA)

    print(f"Rows: {len(df):,}  Columns: {df.shape[1]}")
    print(f"Unique orders: {df['Order_ID'].nunique():,}  Unique products: {df['Product_Name'].nunique():,}")
    print(f"Total sales: {df['Sales'].sum():,.2f}  Total profit: {df['Profit'].sum():,.2f}")
    print(f"Loss-making orders: {(df['Profit'] < 0).mean():.1%}")
    print(f"Sales/Profit correlation: {df['Sales'].corr(df['Profit']):.2f}\n")

    for col in ["Customer_Segment", "Product_Category", "Region", "Ship_Mode"]:
        summary = (
            df.groupby(col)
            .agg(orders=("Sales", "size"), sales=("Sales", "sum"), profit=("Profit", "sum"))
            .sort_values("profit", ascending=False)
        )
        print(summary.round(2), "\n")

    # 1. Orders by customer segment
    fig, ax = plt.subplots(figsize=(6, 6))
    counts = df["Customer_Segment"].value_counts()
    ax.pie(counts, labels=counts.index, autopct="%.1f%%", explode=[0.05] * len(counts), startangle=90)
    ax.set_title("Orders by customer segment")
    save(fig, "01_customer_segment")

    # 2. Orders by product category
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(data=df, x="Product_Category", order=df["Product_Category"].value_counts().index, ax=ax)
    ax.set(title="Orders by product category", xlabel="", ylabel="Orders")
    save(fig, "02_product_category")

    # 3. Orders by ship mode
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(data=df, x="Ship_Mode", order=df["Ship_Mode"].value_counts().index, ax=ax)
    ax.set(title="Orders by ship mode", xlabel="", ylabel="Orders")
    save(fig, "03_ship_mode")

    # 4. Sales vs profit
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="Sales", y="Profit", hue="Product_Category", alpha=0.7, ax=ax)
    ax.axhline(0, color="grey", linewidth=0.8)
    ax.set_title("Sales vs profit by product category")
    save(fig, "04_sales_vs_profit")

    # 5. Profit distribution by category
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="Product_Category", y="Profit", ax=ax)
    ax.set(title="Profit distribution by product category", xlabel="")
    save(fig, "05_profit_by_category")

    # 6. Total profit by region
    fig, ax = plt.subplots(figsize=(10, 5))
    region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
    sns.barplot(x=region.index, y=region.values, ax=ax)
    ax.set(title="Total profit by region", xlabel="", ylabel="Profit")
    ax.tick_params(axis="x", rotation=45)
    save(fig, "06_profit_by_region")

    # 7. Total sales by customer segment
    fig, ax = plt.subplots(figsize=(7, 4))
    seg = df.groupby("Customer_Segment")["Sales"].sum().sort_values(ascending=False)
    sns.barplot(x=seg.index, y=seg.values, ax=ax)
    ax.set(title="Total sales by customer segment", xlabel="", ylabel="Sales")
    save(fig, "07_sales_by_segment")

    # 8. Profit distribution
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["Profit"], kde=True, ax=ax)
    ax.set_title("Profit distribution")
    save(fig, "08_profit_distribution")

    print(f"Charts saved to {OUT}")


if __name__ == "__main__":
    main()
