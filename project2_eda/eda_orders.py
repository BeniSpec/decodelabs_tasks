import pandas as pd


def load_cleaned_data(path="../data/processed/orders_cleaned.csv"):
    return pd.read_csv(path, parse_dates=["Date"])


def compare_mean_median(df, col="TotalPrice"):
    print(f"{col} mean: {df[col].mean():.2f}")
    print(f"{col} median: {df[col].median():.2f}")

if __name__ == "__main__":
    df = load_cleaned_data()
    print(df.shape)
    print(df.head())
    print(df.describe())

import matplotlib.pyplot as plt

def plot_price_distribution(df):
    plt.figure(figsize=(8, 5))
    df["UnitPrice"].hist(bins=30)
    plt.title("Distribution of UnitPrice")
    plt.xlabel("UnitPrice")
    plt.ylabel("Number of Orders")
    plt.savefig("charts/unitprice_distribution.png")
    plt.close()

def plot_quantity_distribution(df):
    plt.figure(figsize=(8, 5))
    df["Quantity"].hist(bins=15)
    plt.title("Distribution of Quantity")
    plt.xlabel("Quantity")
    plt.ylabel("Number of Orders")
    plt.savefig("charts/quantity_distribution.png")
    plt.close()

def plot_price_boxplot(df):
    plt.figure(figsize=(6, 5))
    df.boxplot(column="UnitPrice")
    plt.title("UnitPrice Outliers")
    plt.savefig("charts/unitprice_boxplot.png")
    plt.close()

def plot_quantity_boxplot(df):
    plt.figure(figsize=(6, 5))
    df.boxplot(column="Quantity")
    plt.title("Quantity Outliers")
    plt.savefig("charts/quantity_boxplot.png")
    plt.close()

def revenue_by_product(df):
    result = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)
    print(result)
    return result