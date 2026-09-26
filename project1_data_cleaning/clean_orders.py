import pandas as pd

def load_data(path="../data/raw/orders_raw.csv"):
    return pd.read_csv(path, parse_dates=["Date"])

if __name__ == "__main__":
    df = load_data()
    print(df.head())