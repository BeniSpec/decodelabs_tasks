import pandas as pd
from clean_orders import clean_dates

def test_clean_dates_converts_to_datetime():
    df = pd.DataFrame({"Date": ["2024-01-05", "2024-02-10"]})
    result = clean_dates(df)
    assert pd.api.types.is_datetime64_any_dtype(result["Date"])