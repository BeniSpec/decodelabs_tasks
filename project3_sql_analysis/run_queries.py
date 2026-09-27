import sqlite3
import os

print("Current working directory:", os.getcwd())
print("Files in this folder:", os.listdir(os.getcwd()))

db_path = "orders.db"
print("Does orders.db exist here?", os.path.exists(db_path))

def run_query(query, db_path="orders.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(query)
    for row in cursor.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    print("Revenue by product:")
    run_query("SELECT Product, SUM(TotalPrice) FROM orders GROUP BY Product ORDER BY 2 DESC")