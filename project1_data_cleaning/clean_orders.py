import pandas as pd

def load_data(path="../data/raw/orders_raw.csv"):
    return pd.read_csv(path, parse_dates=["Date"])

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print("Shape:", df.shape)
    print(df.dtypes)
    print("Missing values per column:")
    print(df.isnull().sum())
    print("Duplicate OrderIDs:", df["OrderID"].duplicated().sum())
    print("Duplicate full rows:", df.duplicated().sum())
    
    calc = df["Quantity"] * df["UnitPrice"]
    mismatches = (calc - df["TotalPrice"]).abs() > 0.01
    print("TotalPrice mismatches:", mismatches.sum())

for col in ["Product", "PaymentMethod", "OrderStatus", "ReferralSource", "CouponCode"]:
        print(col, "->", df[col].unique())
        
def standardize_columns(df):
    df.columns = [c.strip() for c in df.columns]
    return df 