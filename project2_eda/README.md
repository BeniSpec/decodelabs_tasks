# Project 2 — Exploratory Data Analysis (EDA)

Goal: explore the cleaned orders dataset to find patterns, trends,
and outliers, and turn them into a short set of business insights.

Uses: data/processed/orders_cleaned.csv (output of Project 1)

Status: complete.

## Note on Correlation
A correlation between two numbers is a clue, not proof that one
causes the other. Any relationship found here should be treated as
something worth investigating further, not a final conclusion.

## Key Findings
- Revenue is led by Chair ($195,620.11), narrowly ahead of Printer ($195,612.61) and Laptop ($192,126.56) — the top 3 products are within about 2% of each other
- 74.2% of orders used a coupon
- 0 orders flagged as Quantity/UnitPrice outliers (IQR method), and 0 TotalPrice outliers by z-score (|z| > 3) — the dataset has no extreme outliers by either method
- Monthly revenue trend is plotted in `charts/monthly_revenue_trend.png` — check that chart for the shape (rising/falling/seasonal), since it wasn't printed to console
- Strongest correlation found: UnitPrice and TotalPrice at 0.72 — makes sense, since TotalPrice is derived partly from UnitPrice

## So What?
- Revenue being split almost evenly across the top 3 products (Chair, Printer, Laptop) suggests the business isn't over-reliant on one hero product — but it also means there's no single "flagship" to double down marketing spend on
- A 74.2% coupon usage rate is high — worth checking whether coupons are actually driving incremental sales or just discounting purchases customers would have made anyway
- Zero outliers by both IQR and z-score methods suggests the order data is clean and consistent, with no single transaction skewing the averages — good sign for trusting the mean/median figures above