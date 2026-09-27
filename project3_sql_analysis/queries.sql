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

-- How does revenue change month to month?
SELECT strftime('%Y-%m', Date) AS Month, SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Month
ORDER BY Month;

-- Which payment method has the highest average order value?
SELECT PaymentMethod, AVG(TotalPrice) AS AvgOrderValue
FROM orders
GROUP BY PaymentMethod
ORDER BY AvgOrderValue DESC;

-- What share of orders used a coupon?
SELECT
    CASE WHEN CouponCode = 'No Coupon' THEN 'No Coupon' ELSE 'Used Coupon' END AS CouponStatus,
    COUNT(*) AS OrderCount
FROM orders
GROUP BY CouponStatus;

-- Which orders were returned, and what were they worth?
SELECT OrderID, CustomerID, Product, TotalPrice
FROM orders
WHERE OrderStatus = 'Returned'
ORDER BY TotalPrice DESC;

-- Which customers have placed more than 1 order and spent over 3000 total?
SELECT CustomerID, COUNT(*) AS OrderCount, SUM(TotalPrice) AS TotalSpent
FROM orders
GROUP BY CustomerID
HAVING COUNT(*) > 1 AND SUM(TotalPrice) > 3000
ORDER BY TotalSpent DESC;