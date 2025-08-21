import pandas as pd
from .query_functions import run_sql

def get_filter_options():
    cities = run_sql('SELECT DISTINCT City FROM providers ORDER BY City')['City'].dropna().tolist()
    provider_types = run_sql('SELECT DISTINCT Type AS Provider_Type FROM providers ORDER BY Provider_Type')['Provider_Type'].tolist()
    food_types = run_sql('SELECT DISTINCT Food_Type FROM food_listings ORDER BY Food_Type')['Food_Type'].tolist()
    meal_types = run_sql('SELECT DISTINCT Meal_Type FROM food_listings ORDER BY Meal_Type')['Meal_Type'].tolist()
    return {
        'cities': cities,
        'provider_types': provider_types,
        'food_types': food_types,
        'meal_types': meal_types
    }

def filtered_food_listings(city=None, provider_type=None, food_type=None, meal_type=None):
    q = 'SELECT * FROM food_listings WHERE 1=1'
    params = {}
    if city:
        q += ' AND Location = :city'
        params['city'] = city
    if provider_type:
        q += ' AND Provider_Type = :ptype'
        params['ptype'] = provider_type
    if food_type:
        q += ' AND Food_Type = :ftype'
        params['ftype'] = food_type
    if meal_type:
        q += ' AND Meal_Type = :mtype'
        params['mtype'] = meal_type
    return run_sql(q, params)
