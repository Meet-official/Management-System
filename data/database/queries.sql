-- 1. Count providers and receivers per city
-- Returns: City, Providers_Count, Receivers_Count
WITH p AS (
  SELECT City, COUNT(*) AS providers_count FROM providers GROUP BY City
),
r AS (
  SELECT City, COUNT(*) AS receivers_count FROM receivers GROUP BY City
)
SELECT COALESCE(p.City, r.City) AS City,
       COALESCE(p.providers_count, 0) AS Providers_Count,
       COALESCE(r.receivers_count, 0) AS Receivers_Count
FROM p
FULL OUTER JOIN r ON p.City = r.City;

-- Note: SQLite lacks FULL OUTER JOIN; the app provides an equivalent using UNION in Python.

-- 2. Provider type contributing the most (by total quantity listed)
SELECT Provider_Type, SUM(Quantity) AS Total_Quantity
FROM food_listings
GROUP BY Provider_Type
ORDER BY Total_Quantity DESC;

-- 3. Contact info of providers in a specific city (:city)
SELECT Name, Type, Address, City, Contact
FROM providers
WHERE City = :city
ORDER BY Name;

-- 4. Receivers with most claims (count of claims)
SELECT rc.Receiver_ID, rc.Name, COUNT(*) AS Total_Claims
FROM claims c
JOIN receivers rc ON rc.Receiver_ID = c.Receiver_ID
GROUP BY rc.Receiver_ID, rc.Name
ORDER BY Total_Claims DESC;

-- 5. Total quantity of food available (by status Available)
SELECT SUM(Quantity) AS Total_Available_Quantity
FROM food_listings
WHERE Status = 'Available';

-- 6. City with highest number of food listings
SELECT Location AS City, COUNT(*) AS Listings
FROM food_listings
GROUP BY Location
ORDER BY Listings DESC;

-- 7. Most common food types
SELECT Food_Type, COUNT(*) AS Count
FROM food_listings
GROUP BY Food_Type
ORDER BY Count DESC;

-- 8. Claims per food item
SELECT f.Food_ID, f.Food_Name, COUNT(c.Claim_ID) AS Claims_Count
FROM food_listings f
LEFT JOIN claims c ON c.Food_ID = f.Food_ID
GROUP BY f.Food_ID, f.Food_Name
ORDER BY Claims_Count DESC;

-- 9. Provider with highest number of completed claims
SELECT p.Provider_ID, p.Name, COUNT(*) AS Completed_Claims
FROM claims c
JOIN food_listings f ON f.Food_ID = c.Food_ID
JOIN providers p ON p.Provider_ID = f.Provider_ID
WHERE c.Status = 'Completed'
GROUP BY p.Provider_ID, p.Name
ORDER BY Completed_Claims DESC;

-- 10. Percentage of claims by status
SELECT Status,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM claims), 2) AS Percentage
FROM claims
GROUP BY Status;

-- 11. Average quantity claimed per receiver
SELECT rc.Receiver_ID, rc.Name, AVG(f.Quantity) AS Avg_Quantity_Claimed
FROM claims c
JOIN receivers rc ON rc.Receiver_ID = c.Receiver_ID
JOIN food_listings f ON f.Food_ID = c.Food_ID
WHERE c.Status IN ('Completed', 'Pending')
GROUP BY rc.Receiver_ID, rc.Name
ORDER BY Avg_Quantity_Claimed DESC;

-- 12. Most claimed meal type
SELECT f.Meal_Type, COUNT(*) AS Claims_Count
FROM claims c
JOIN food_listings f ON f.Food_ID = c.Food_ID
GROUP BY f.Meal_Type
ORDER BY Claims_Count DESC;

-- 13. Total quantity donated by each provider
SELECT p.Provider_ID, p.Name, SUM(f.Quantity) AS Total_Donated_Quantity
FROM food_listings f
JOIN providers p ON p.Provider_ID = f.Provider_ID
GROUP BY p.Provider_ID, p.Name
ORDER BY Total_Donated_Quantity DESC;

-- 14. Near-expiry items (<= 2 days from :today)
SELECT Food_ID, Food_Name, Quantity, Expiry_Date, Location
FROM food_listings
WHERE julianday(Expiry_Date) - julianday(:today) BETWEEN 0 AND 2
ORDER BY Expiry_Date;

-- 15. Claim completion rate over time (by month)
SELECT strftime('%Y-%m', Timestamp) AS YearMonth,
       SUM(CASE WHEN Status='Completed' THEN 1 ELSE 0 END) AS Completed,
       SUM(CASE WHEN Status='Pending' THEN 1 ELSE 0 END) AS Pending,
       SUM(CASE WHEN Status='Cancelled' THEN 1 ELSE 0 END) AS Cancelled
FROM claims
GROUP BY YearMonth
ORDER BY YearMonth;
