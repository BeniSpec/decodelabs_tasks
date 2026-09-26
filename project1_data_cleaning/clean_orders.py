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
 
def trim_text_columns(df):
    text_cols = ["Product", "ShippingAddress", "PaymentMethod",
                 "OrderStatus", "ReferralSource", "CouponCode"]
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()
    return df

def standardize_payment_method(df):
    df["PaymentMethod"] = df["PaymentMethod"].str.title()
    return df
def standardize_product(df):
    df["Product"] = df["Product"].str.title()
    return df
def standardize_order_status(df):
    df["OrderStatus"] = df["OrderStatus"].str.title()
    return df

def clean_dates(df):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df

def fill_missing_coupon(df):
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
    return df

def flag_quantity_outliers(df):
    q1, q3 = df["Quantity"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["QuantityOutlier"] = ~df["Quantity"].between(lower, upper)
    return df

def flag_price_outliers(df):
    q1, q3 = df["UnitPrice"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["PriceOutlier"] = ~df["UnitPrice"].between(lower, upper)
    return df

def check_repeat_customers(df):
    counts = df["CustomerID"].value_counts()
    print("Repeat customers:", (counts > 1).sum())
    return df

def validate_tracking_number(df):
    valid = df["TrackingNumber"].str.match(r"^TRK\d+$")
    print("Invalid tracking numbers:", (~valid).sum())
    return df

def add_order_month(df):
    df["OrderMonth"] = df["Date"].dt.to_period("M").astype(str)
    return df

def add_order_year(df):
    df["OrderYear"] = df["Date"].dt.year
    return df

def add_repeat_customer_flag(df):
    counts = df["CustomerID"].value_counts()
    df["IsRepeatCustomer"] = df["CustomerID"].map(counts) > 1
    return df

def add_has_coupon_flag(df):
    df["HasCoupon"] = df["CouponCode"] != "No Coupon"
    return df

def add_customer_avg_order_value(df):
    avg = df.groupby("CustomerID")["TotalPrice"].transform("mean")
    df["CustomerAvgOrderValue"] = avg.round(2)
    return df

# Combine everything into one pipeline function
def clean_data(df):
    df = standardize_columns(df)
    df = trim_text_columns(df)
    df = standardize_product(df)
    df = standardize_payment_method(df)
    df = standardize_order_status(df)
    df = clean_dates(df)
    df = fill_missing_coupon(df)
    df = flag_quantity_outliers(df)
    df = flag_price_outliers(df)
    df = validate_tracking_number(df)
    df = add_order_month(df)
    df = add_order_year(df)
    df = add_repeat_customer_flag(df)
    df = add_has_coupon_flag(df)
    df = add_customer_avg_order_value(df)
    return df

def check_row_count(before, after):
    print(f"Rows before: {len(before)}, after: {len(after)}")
    assert len(before) == len(after), "Row count changed unexpectedly"