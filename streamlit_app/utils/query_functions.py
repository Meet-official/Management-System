import os
import pandas as pd
from .db_connection import get_connection

def run_sql(query: str, params: dict | None = None) -> pd.DataFrame:
    con = get_connection()
    try:
        df = pd.read_sql_query(query, con, params=params)
        return df
    finally:
        con.close()

def providers_receivers_by_city() -> pd.DataFrame:
    # SQLite doesn't support FULL OUTER JOIN; use UNION of LEFT JOINs
    q = '''
    SELECT p.City AS City,
           COUNT(p.Provider_ID) AS Providers_Count,
           COALESCE(r.Receivers_Count, 0) AS Receivers_Count
    FROM providers p
    LEFT JOIN (
        SELECT City, COUNT(*) AS Receivers_Count FROM receivers GROUP BY City
    ) r ON r.City = p.City
    GROUP BY p.City

    UNION

    SELECT r.City AS City,
           COALESCE(p.Providers_Count, 0) AS Providers_Count,
           COUNT(r.Receiver_ID) AS Receivers_Count
    FROM receivers r
    LEFT JOIN (
        SELECT City, COUNT(*) AS Providers_Count FROM providers GROUP BY City
    ) p ON p.City = r.City
    WHERE r.City NOT IN (SELECT City FROM providers)
    GROUP BY r.City
    '''
    return run_sql(q)

def top_provider_types() -> pd.DataFrame:
    q = '''
    SELECT Provider_Type, SUM(Quantity) AS Total_Quantity
    FROM food_listings
    GROUP BY Provider_Type
    ORDER BY Total_Quantity DESC
    '''
    return run_sql(q)

def provider_contacts_by_city(city: str) -> pd.DataFrame:
    q = 'SELECT Name, Type, Address, City, Contact FROM providers WHERE City = :city ORDER BY Name'
    return run_sql(q, {'city': city})

def top_receivers_by_claims() -> pd.DataFrame:
    q = '''
    SELECT rc.Receiver_ID, rc.Name, COUNT(*) AS Total_Claims
    FROM claims c
    JOIN receivers rc ON rc.Receiver_ID = c.Receiver_ID
    GROUP BY rc.Receiver_ID, rc.Name
    ORDER BY Total_Claims DESC
    '''
    return run_sql(q)

def total_available_quantity() -> pd.DataFrame:
    q = "SELECT SUM(Quantity) AS Total_Available_Quantity FROM food_listings WHERE Status='Available'"
    return run_sql(q)

def city_with_most_listings() -> pd.DataFrame:
    q = 'SELECT Location AS City, COUNT(*) AS Listings FROM food_listings GROUP BY Location ORDER BY Listings DESC'
    return run_sql(q)

def most_common_food_types() -> pd.DataFrame:
    q = 'SELECT Food_Type, COUNT(*) AS Count FROM food_listings GROUP BY Food_Type ORDER BY Count DESC'
    return run_sql(q)

def claims_per_food_item() -> pd.DataFrame:
    q = '''
    SELECT f.Food_ID, f.Food_Name, COUNT(c.Claim_ID) AS Claims_Count
    FROM food_listings f
    LEFT JOIN claims c ON c.Food_ID = f.Food_ID
    GROUP BY f.Food_ID, f.Food_Name
    ORDER BY Claims_Count DESC
    '''
    return run_sql(q)

def provider_with_most_completed_claims() -> pd.DataFrame:
    q = '''
    SELECT p.Provider_ID, p.Name, COUNT(*) AS Completed_Claims
    FROM claims c
    JOIN food_listings f ON f.Food_ID = c.Food_ID
    JOIN providers p ON p.Provider_ID = f.Provider_ID
    WHERE c.Status = 'Completed'
    GROUP BY p.Provider_ID, p.Name
    ORDER BY Completed_Claims DESC
    '''
    return run_sql(q)

def claims_percentage_by_status() -> pd.DataFrame:
    q = '''
    SELECT Status,
           ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM claims), 2) AS Percentage
    FROM claims
    GROUP BY Status
    '''
    return run_sql(q)

def avg_quantity_claimed_per_receiver() -> pd.DataFrame:
    q = '''
    SELECT rc.Receiver_ID, rc.Name, AVG(f.Quantity) AS Avg_Quantity_Claimed
    FROM claims c
    JOIN receivers rc ON rc.Receiver_ID = c.Receiver_ID
    JOIN food_listings f ON f.Food_ID = c.Food_ID
    WHERE c.Status IN ('Completed', 'Pending')
    GROUP BY rc.Receiver_ID, rc.Name
    ORDER BY Avg_Quantity_Claimed DESC
    '''
    return run_sql(q)

def most_claimed_meal_type() -> pd.DataFrame:
    q = '''
    SELECT f.Meal_Type, COUNT(*) AS Claims_Count
    FROM claims c
    JOIN food_listings f ON f.Food_ID = c.Food_ID
    GROUP BY f.Meal_Type
    ORDER BY Claims_Count DESC
    '''
    return run_sql(q)

def total_quantity_by_provider() -> pd.DataFrame:
    q = '''
    SELECT p.Provider_ID, p.Name, SUM(f.Quantity) AS Total_Donated_Quantity
    FROM food_listings f
    JOIN providers p ON p.Provider_ID = f.Provider_ID
    GROUP BY p.Provider_ID, p.Name
    ORDER BY Total_Donated_Quantity DESC
    '''
    return run_sql(q)

def near_expiry_items(today_iso: str) -> pd.DataFrame:
    q = '''
    SELECT Food_ID, Food_Name, Quantity, Expiry_Date, Location
    FROM food_listings
    WHERE julianday(Expiry_Date) - julianday(:today) BETWEEN 0 AND 2
    ORDER BY Expiry_Date
    '''
    return run_sql(q, {'today': today_iso})

def claim_completion_rate_over_time() -> pd.DataFrame:
    q = '''
    SELECT strftime('%Y-%m', Timestamp) AS YearMonth,
           SUM(CASE WHEN Status='Completed' THEN 1 ELSE 0 END) AS Completed,
           SUM(CASE WHEN Status='Pending' THEN 1 ELSE 0 END) AS Pending,
           SUM(CASE WHEN Status='Cancelled' THEN 1 ELSE 0 END) AS Cancelled
    FROM claims
    GROUP BY YearMonth
    ORDER BY YearMonth
    '''
    return run_sql(q)
