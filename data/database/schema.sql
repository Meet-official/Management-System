-- Schema for Local Food Wastage Management System (SQLite)
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS providers (
    Provider_ID     INTEGER PRIMARY KEY,
    Name            TEXT NOT NULL,
    Type            TEXT NOT NULL,
    Address         TEXT,
    City            TEXT NOT NULL,
    Contact         TEXT
);

CREATE TABLE IF NOT EXISTS receivers (
    Receiver_ID     INTEGER PRIMARY KEY,
    Name            TEXT NOT NULL,
    Type            TEXT NOT NULL,
    City            TEXT NOT NULL,
    Contact         TEXT
);

CREATE TABLE IF NOT EXISTS food_listings (
    Food_ID         INTEGER PRIMARY KEY,
    Food_Name       TEXT NOT NULL,
    Quantity        INTEGER NOT NULL CHECK (Quantity >= 0),
    Expiry_Date     TEXT NOT NULL,          -- ISO date string YYYY-MM-DD
    Provider_ID     INTEGER NOT NULL,
    Provider_Type   TEXT NOT NULL,
    Location        TEXT NOT NULL,          -- City where food is available
    Food_Type       TEXT NOT NULL,          -- Vegetarian / Non-Vegetarian / Vegan
    Meal_Type       TEXT NOT NULL,          -- Breakfast / Lunch / Dinner / Snacks
    Status          TEXT DEFAULT 'Available', -- Available / Claimed / Expired
    FOREIGN KEY (Provider_ID) REFERENCES providers(Provider_ID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS claims (
    Claim_ID        INTEGER PRIMARY KEY,
    Food_ID         INTEGER NOT NULL,
    Receiver_ID     INTEGER NOT NULL,
    Status          TEXT NOT NULL,          -- Pending / Completed / Cancelled
    Timestamp       TEXT NOT NULL,          -- ISO datetime string
    FOREIGN KEY (Food_ID) REFERENCES food_listings(Food_ID) ON DELETE CASCADE,
    FOREIGN KEY (Receiver_ID) REFERENCES receivers(Receiver_ID) ON DELETE CASCADE
);

-- Useful indexes
CREATE INDEX IF NOT EXISTS idx_providers_city ON providers(City);
CREATE INDEX IF NOT EXISTS idx_receivers_city ON receivers(City);
CREATE INDEX IF NOT EXISTS idx_food_location ON food_listings(Location);
CREATE INDEX IF NOT EXISTS idx_food_provider ON food_listings(Provider_ID);
CREATE INDEX IF NOT EXISTS idx_claims_food ON claims(Food_ID);
CREATE INDEX IF NOT EXISTS idx_claims_receiver ON claims(Receiver_ID);
