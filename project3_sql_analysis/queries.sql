-- Sanity check: confirm the table loaded correctly
SELECT * FROM orders LIMIT 10;

-- Which products bring in the most revenue?
SELECT Product, SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;

-- How many orders fall into each status?
SELECT OrderStatus, COUNT(*) AS OrderCount
FROM orders
GROUP BY OrderStatus
ORDER BY OrderCount DESC;

-- Who are the highest-spending customers?
SELECT CustomerID, SUM(TotalPrice) AS TotalSpent
FROM orders
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 10;