# Project 3 — SQL Data Analysis

Goal: load the cleaned orders dataset into a small SQL database and
answer specific business questions using SQL queries.

Uses: data/processed/orders_cleaned.csv (output of Project 1)

Status: in progress.

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
| [fill in top product] | [fill in actual number] |
| [fill in second product] | [fill in actual number] |