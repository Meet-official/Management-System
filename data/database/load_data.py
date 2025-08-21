import os
import sqlite3
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(ROOT, 'data', 'database', 'food.db')
SCHEMA_PATH = os.path.join(ROOT, 'data', 'database', 'schema.sql')

CSV_DIR = os.path.join(ROOT, 'data')
PROVIDERS_CSV = os.path.join(CSV_DIR, 'providers_data.csv')
RECEIVERS_CSV = os.path.join(CSV_DIR, 'receivers_data.csv')
FOOD_CSV = os.path.join(CSV_DIR, 'food_listings_data.csv')
CLAIMS_CSV = os.path.join(CSV_DIR, 'claims_data.csv')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        con.executescript(f.read())
    con.commit()
    con.close()

def load_csv_to_sql():
    con = sqlite3.connect(DB_PATH)

    def load(csv_path, table):
        if not os.path.exists(csv_path):
            print(f'[WARN] Missing CSV: {csv_path} -> skipping {table}')
            return
        df = pd.read_csv(csv_path)
        # Normalize column names to strip spaces
        df.columns = [c.strip() for c in df.columns]
        df.to_sql(table, con, if_exists='append', index=False)
        print(f'[OK] Loaded {len(df)} rows into {table}')

    load(PROVIDERS_CSV, 'providers')
    load(RECEIVERS_CSV, 'receivers')
    load(FOOD_CSV, 'food_listings')
    load(CLAIMS_CSV, 'claims')

    con.close()

if __name__ == '__main__':
    init_db()
    load_csv_to_sql()
    print('Database initialized and CSVs loaded. DB at:', DB_PATH)
