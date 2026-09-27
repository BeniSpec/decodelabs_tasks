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

def plot_revenue_by_product(df):
    revenue = revenue_by_product(df)
    plt.figure(figsize=(8, 5))
    revenue.plot(kind="bar")
    plt.title("Revenue by Product")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.savefig("charts/revenue_by_product.png")
    plt.close()

def monthly_revenue_trend(df):
    df["OrderMonth"] = df["Date"].dt.to_period("M").astype(str)
    trend = df.groupby("OrderMonth")["TotalPrice"].sum()
    return trend

def plot_monthly_trend(df):
    trend = monthly_revenue_trend(df)
    plt.figure(figsize=(10, 5))
    trend.plot(kind="line", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/monthly_revenue_trend.png")
    plt.close()

def plot_revenue_by_payment_method(df):
    revenue = df.groupby("PaymentMethod")["TotalPrice"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    revenue.plot(kind="bar")
    plt.title("Revenue by Payment Method")
    plt.tight_layout()
    plt.savefig("charts/revenue_by_payment_method.png")
    plt.close()

def plot_order_status_breakdown(df):
    counts = df["OrderStatus"].value_counts()
    plt.figure(figsize=(7, 5))
    counts.plot(kind="bar")
    plt.title("Orders by Status")
    plt.tight_layout()
    plt.savefig("charts/order_status_breakdown.png")
    plt.close()

def plot_referral_source_breakdown(df):
    counts = df["ReferralSource"].value_counts()
    plt.figure(figsize=(7, 5))
    counts.plot(kind="bar")
    plt.title("Orders by Referral Source")
    plt.tight_layout()
    plt.savefig("charts/referral_source_breakdown.png")
    plt.close()

def coupon_usage_rate(df):
    used = (df["HasCoupon"]).sum()
    rate = used / len(df) * 100
    print(f"Coupon usage rate: {rate:.1f}%")
    return rate

def iqr_outlier_summary(df):
    print("Quantity outliers (IQR method):", df["QuantityOutlier"].sum())
    print("UnitPrice outliers (IQR method):", df["PriceOutlier"].sum())

def zscore_outliers(df, col="TotalPrice"):
    mean, std = df[col].mean(), df[col].std()
    z = (df[col] - mean) / std
    flagged = (z.abs() > 3).sum()
    print(f"{col} z-score outliers (|z| > 3): {flagged}")
    return flagged

def correlation_matrix(df):
    numeric_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
    corr = df[numeric_cols].corr()
    print(corr)
    return corr