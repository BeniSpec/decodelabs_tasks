import sqlite3
import pandas as pd

def build_database(csv_path="../data/processed/orders_cleaned.csv",
                    db_path="orders.db"):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()
    print("Database built:", db_path)

if __name__ == "__main__":
    build_database()
