# Data Quality Report — Initial Audit

- Rows: 1200, Columns: 14
- No duplicate OrderIDs, no duplicate rows
- TotalPrice matches Quantity × UnitPrice for all rows
- CouponCode has 309 missing values (customers who used no coupon)
- Categories (Product, PaymentMethod, OrderStatus, ReferralSource)
  are already consistent — no typos or case mismatches found