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