# Project 3 — SQL Data Analysis

Goal: load the cleaned orders dataset into a small SQL database and
answer specific business questions using SQL queries.

Uses: data/processed/orders_cleaned.csv (output of Project 1)

Status: complete.

## A Note on Query Order
SQL doesn't run top to bottom the way you read it. The database
processes FROM and WHERE before SELECT, which is why you can't
filter using a column alias you just created in SELECT — that alias
doesn't exist yet at the point WHERE runs.

## How to Run
```bash
pip install pandas
python build_db.py
python run_queries.py
```
## Sample Result: Revenue by Product
| Product | Revenue |
|---|---|
| Chair | $195,620.11 |
| Printer | $195,612.61 |

## Query Index
1. Revenue by product — which products earn the most
2. Orders by status — order pipeline health
3. Top 10 customers — who to prioritize for retention
4. Monthly revenue trend — is the business growing
5. Average order value by payment method — payment behavior
6. Coupon usage rate — promotion effectiveness
7. Returned orders — where losses are happening
8. High-value repeat customers — best customers to reward
9. Top products by average quantity — bulk-buy items
10. Revenue by referral source — best marketing channels
11. Above-average orders — high-value order patterns
12. Best product per payment method — cross-analysis