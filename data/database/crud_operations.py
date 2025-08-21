import os
import sqlite3
from typing import Dict, Any

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(ROOT, 'data', 'database', 'food.db')

def get_connection():
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    return con

# ---------- Providers ----------
def add_provider(data: Dict[str, Any]):
    with get_connection() as con:
        con.execute(
            'INSERT INTO providers (Provider_ID, Name, Type, Address, City, Contact) VALUES (?, ?, ?, ?, ?, ?)',
            (data.get('Provider_ID'), data['Name'], data['Type'], data.get('Address'), data['City'], data.get('Contact'))
        )

def update_provider(provider_id: int, updates: Dict[str, Any]):
    keys = ', '.join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values()) + [provider_id]
    with get_connection() as con:
        con.execute(f'UPDATE providers SET {keys} WHERE Provider_ID = ?', values)

def delete_provider(provider_id: int):
    with get_connection() as con:
        con.execute('DELETE FROM providers WHERE Provider_ID = ?', (provider_id,))

# ---------- Receivers ----------
def add_receiver(data: Dict[str, Any]):
    with get_connection() as con:
        con.execute(
            'INSERT INTO receivers (Receiver_ID, Name, Type, City, Contact) VALUES (?, ?, ?, ?, ?)',
            (data.get('Receiver_ID'), data['Name'], data['Type'], data['City'], data.get('Contact'))
        )

def update_receiver(receiver_id: int, updates: Dict[str, Any]):
    keys = ', '.join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values()) + [receiver_id]
    with get_connection() as con:
        con.execute(f'UPDATE receivers SET {keys} WHERE Receiver_ID = ?', values)

def delete_receiver(receiver_id: int):
    with get_connection() as con:
        con.execute('DELETE FROM receivers WHERE Receiver_ID = ?', (receiver_id,))

# ---------- Food Listings ----------
def add_food_listing(data: Dict[str, Any]):
    with get_connection() as con:
        con.execute(
            '''INSERT INTO food_listings
               (Food_ID, Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type, Status)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (data.get('Food_ID'), data['Food_Name'], data['Quantity'], data['Expiry_Date'],
             data['Provider_ID'], data['Provider_Type'], data['Location'], data['Food_Type'],
             data['Meal_Type'], data.get('Status', 'Available'))
        )

def update_food_listing(food_id: int, updates: Dict[str, Any]):
    keys = ', '.join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values()) + [food_id]
    with get_connection() as con:
        con.execute(f'UPDATE food_listings SET {keys} WHERE Food_ID = ?', values)

def delete_food_listing(food_id: int):
    with get_connection() as con:
        con.execute('DELETE FROM food_listings WHERE Food_ID = ?', (food_id,))

# ---------- Claims ----------
def add_claim(data: Dict[str, Any]):
    with get_connection() as con:
        con.execute(
            'INSERT INTO claims (Claim_ID, Food_ID, Receiver_ID, Status, Timestamp) VALUES (?, ?, ?, ?, ?)',
            (data.get('Claim_ID'), data['Food_ID'], data['Receiver_ID'], data['Status'], data['Timestamp'])
        )

def update_claim(claim_id: int, updates: Dict[str, Any]):
    keys = ', '.join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values()) + [claim_id]
    with get_connection() as con:
        con.execute(f'UPDATE claims SET {keys} WHERE Claim_ID = ?', values)

def delete_claim(claim_id: int):
    with get_connection() as con:
        con.execute('DELETE FROM claims WHERE Claim_ID = ?', (claim_id,))
