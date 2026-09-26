# Project 1 — Data Cleaning & Preparation

Goal: audit and clean the raw orders dataset so it is reliable for
analysis in Projects 2 and 3.

Status: in progress.

## Methodology
1. Audited the raw dataset for missing values, duplicates, and
   inconsistent formatting.
2. Standardized text fields and dates.
3. Filled missing CouponCode values with a meaningful label.
4. Flagged (not deleted) statistical outliers for review.
5. Added derived columns useful for later analysis.
6. Validated the result and exported the cleaned dataset.

## How to Run
```bash
pip install -r ../requirements.txt
python clean_orders.py
```

## Sample of Cleaned Data
| OrderID | Date | Product | TotalPrice | HasCoupon |
|---|---|---|---|---|
| ORD200000 | 2023-01-04 | Monitor | 2853.10 | True |