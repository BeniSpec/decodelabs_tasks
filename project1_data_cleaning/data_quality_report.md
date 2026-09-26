# Data Quality Report — Initial Audit

- Rows: 1200, Columns: 14
- No duplicate OrderIDs, no duplicate rows
- TotalPrice matches Quantity × UnitPrice for all rows
- CouponCode has 309 missing values (customers who used no coupon)
- Categories (Product, PaymentMethod, OrderStatus, ReferralSource)
  are already consistent — no typos or case mismatches found

## Final Results
- Rows cleaned: 1200 (no rows dropped)
- Missing CouponCode values replaced with "No Coupon": 309
- Quantity outliers flagged: [fill in your actual number]
- UnitPrice outliers flagged: [fill in your actual number]
- All post-cleaning checks passed (no nulls, no duplicates)

## Change Log
| Change | Reason | Impact |
|---|---|---|
| Filled missing CouponCode | Missing meant "no coupon used" | 309 rows updated |
| Standardized text casing | Consistency for grouping/analysis | All text columns |
| Flagged Quantity/Price outliers | Separate real extremes from errors | Marked, not deleted |