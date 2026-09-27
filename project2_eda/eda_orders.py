import pandas as pd

def load_cleaned_data(path="../data/processed/orders_cleaned.csv"):
    return pd.read_csv(path, parse_dates=["Date"])

if __name__ == "__main__":
    df = load_cleaned_data()
    print(df.shape)
    print(df.head())