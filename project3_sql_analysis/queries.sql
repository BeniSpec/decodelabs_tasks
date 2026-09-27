-- Sanity check: confirm the table loaded correctly
SELECT * FROM orders LIMIT 10;

-- Which products bring in the most revenue?
SELECT Product, SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;