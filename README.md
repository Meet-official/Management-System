# Local Food Waste Management System
## 🌐 Live Web App: [Open app in new tab](https://mit-management-system.streamlit.app/)

---

## 📖 Overview

Food waste is a pressing global issue---large quantities of edible food
are discarded daily, while many people struggle with hunger and food
insecurity.
This project introduces a **Local Food Waste Management System** built
with **Python, SQL, and Streamlit**, aiming to minimize waste and
promote social welfare.

The system enables: - **Providers** (restaurants, grocery stores,
households) to list surplus food.
- **Receivers** (NGOs, individuals, community centers) to request and
collect available food.
- **Admins** to oversee and manage providers, receivers, food items, and
claims via **CRUD operations**. 
- **Data-driven insights** through SQL queries and exploratory data
analysis (EDA).

By combining **data engineering, analytics, and web app development**,
this project delivers a scalable solution to reduce waste and support
communities.

------------------------------------------------------------------------

## 🛠 Skills Acquired

-   Python programming 
-   SQL schema design & querying 
-   CRUD operations 
-   Data cleaning & preparation 
-   Exploratory Data Analysis (EDA) 
-   Streamlit application development 
-   Dashboarding & visualization

------------------------------------------------------------------------

## 🌍 Domain

-   Food Management 
-   Waste Reduction 
-   Social Good / Community Welfare

------------------------------------------------------------------------

## 🚨 Problem Statement

Despite abundant food supply, wastage is widespread. Restaurants and
households frequently discard edible food, while many communities face
food insecurity.

This project creates a **centralized system** to: 
- Connect **providers** with **receivers**. 
- Redistribute surplus food efficiently. 
- Generate insights into food waste patterns for better decision-making.

------------------------------------------------------------------------

## 💡 Business Applications

-   Optimized redistribution of surplus food 
-   Increased transparency in donations 
-   Data-driven support for policy-making and donation drives 
-   Easier food access for NGOs and communities

------------------------------------------------------------------------

## ⚙️ Running Locally

``` bash
# 1) Install required dependencies
pip install -r requirements.txt

# 2) Initialize database and load CSVs (place your 4 CSV files under /data/ with exact filenames)
python data/database/load_data.py

# 3) Launch Streamlit app
python -m streamlit run streamlit_app/app.py
```

### 🔑 Notes

-   The project uses **SQLite** (`food.db`) by default. For production,
    switch to PostgreSQL/MySQL by updating the connection utilities. 
-   Ensure your CSV headers match the dataset schema.

------------------------------------------------------------------------

## 🔎 Methodology & Approach

### 1. Data Preparation

-   Collected CSV datasets for providers, receivers, food listings, and
    claims. 
-   Cleaned and standardized datasets for consistency.

### 2. Database Schema & Setup

-   Designed SQL schema for 4 core entities:
    -   Providers 
    -   Receivers 
    -   Food Listings 
    -   Claims 
-   Imported cleaned datasets into SQL tables.

### 3. Data Analysis

-   Wrote **15 SQL queries** to answer critical business questions. 
-   Conducted **EDA** to identify provider contributions, food
    distribution, and wastage trends.

### 4. Application Development

-   Built a **Streamlit dashboard** supporting:
    -   Food filtering (city, provider type, food type, meal type) 
    -   Provider contact info display 
    -   CRUD functionality 
    -   SQL-powered insights visualization

### 5. Deployment

-   Streamlit app deployed for interactive and real-time use.

------------------------------------------------------------------------

## 🏗 Data Flow & Architecture

**Data Source** → CSVs → SQL Database (Providers, Receivers, Food
Listings, Claims) 
**Processing Layer** → SQL Queries + Python Data Analysis 
**Application Layer** → Streamlit UI (CRUD + Filtering + Visualizations)

------------------------------------------------------------------------

## 📂 Dataset Description

### 1. Providers Dataset (`providers.csv`)

  Column        Description
  ------------- -------------------------------------
  Provider_ID   Unique identifier
  Name          Provider name (restaurant, grocery)
  Type          Type of provider
  Address       Provider address
  City          Provider's city
  Contact       Contact details

### 2. Receivers Dataset (`receivers.csv`)

  Column        Description
  ------------- -----------------------------
  Receiver_ID   Unique identifier
  Name          Receiver name (NGO, person)
  Type          Receiver type
  City          City of receiver
  Contact       Contact details

### 3. Food Listings Dataset (`food_listings.csv`)

  Column          Description
  --------------- ----------------------------
  Food_ID         Unique identifier
  Food_Name       Food item name
  Quantity        Available quantity
  Expiry_Date     Expiration date
  Provider_ID     Linked provider ID
  Provider_Type   Type of provider
  Location        City
  Food_Type       Veg / Non-Veg / Vegan
  Meal_Type       Breakfast / Lunch / Dinner

### 4. Claims Dataset (`claims.csv`)

  Column        Description
  ------------- --------------------------------------------
  Claim_ID      Unique identifier
  Food_ID       Linked food item ID
  Receiver_ID   Linked receiver ID
  Status        Claim status (Pending/Completed/Cancelled)
  Timestamp     Claim creation date & time

------------------------------------------------------------------------

## ❓ Key SQL Queries

1.  Providers & receivers by city 
2.  Top provider types contributing food 
3.  Provider contact details by city 
4.  Most active receivers 
5.  Total available food quantity 
6.  Cities with maximum food listings 
7.  Commonly donated food types 
8.  Claims per food item 
9.  Providers with most successful claims 
10. Claim status distribution 
11. Avg quantity claimed per receiver 
12. Meal types with highest claims 
13. Total food donated per provider 
14. Food expiry trends 
15. High-wastage locations

------------------------------------------------------------------------

## 📊 Results & Insights

✅ **Working Streamlit Application** 
- Food listing search & filters 
- CRUD operations for all entities 
- SQL query visualizations

✅ **SQL-Driven Analytics** 
- Provider contribution trends 
- Receiver engagement 
- Claim success metrics 
- Food waste reduction insights

------------------------------------------------------------------------

## 📏 Evaluation Metrics

-   Completeness of SQL database 
-   Accuracy of queries 
-   Functionality of CRUD operations 
-   Usability of Streamlit UI 
-   Effectiveness of EDA visualizations

------------------------------------------------------------------------

## 🧰 Tech Stack

-   **Python** -- Data processing & logic 
-   **SQL** -- Database & queries 
-   **Streamlit** -- Web app interface 
-   **Pandas / Matplotlib** -- Data cleaning & visualization

------------------------------------------------------------------------

## 🚀 Deliverables

-   Cleaned datasets (CSV files) 
-   SQL schema & 15 business queries 
-   Streamlit app with:
    -   EDA dashboard 
    -   CRUD operations 
    -   Query results viewer 
-   Documentation (README, schema, insights)

------------------------------------------------------------------------

## 📌 Tags

`Python` `SQL` `Streamlit` `Data Analysis` `Food Management`
`Waste Reduction` `Social Good`
