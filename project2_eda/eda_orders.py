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