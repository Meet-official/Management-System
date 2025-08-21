import os
import sqlite3
from contextlib import contextmanager

# Point to the SQLite DB inside data/database/food.db
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(ROOT, 'data', 'database', 'food.db')

def get_connection():
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    return con

@contextmanager
def db_cursor():
    con = get_connection()
    cur = con.cursor()
    try:
        yield cur
        con.commit()
    finally:
        cur.close()
        con.close()
