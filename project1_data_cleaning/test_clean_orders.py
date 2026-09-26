import pandas as pd
from clean_orders import clean_dates

def test_clean_dates_converts_to_datetime():
    df = pd.DataFrame({"Date": ["2024-01-05", "2024-02-10"]})
    result = clean_dates(df)
    assert pd.api.types.is_datetime64_any_dtype(result["Date"])

from clean_orders import fill_missing_coupon

def test_fill_missing_coupon_replaces_nan():
    df = pd.DataFrame({"CouponCode": ["SAVE10", None]})
    result = fill_missing_coupon(df)
    assert result["CouponCode"].isnull().sum() == 0

def clean_data(df):
    print("Standardizing columns...")
    df = standardize_columns(df)
    print("Trimming text fields...")
    df = trim_text_columns(df)
    # (keep the rest of the calls, just add a print line above each one)