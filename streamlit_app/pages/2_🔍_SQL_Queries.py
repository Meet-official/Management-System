import streamlit as st
import pandas as pd
from utils.query_functions import (
    providers_receivers_by_city, top_provider_types, provider_contacts_by_city,
    top_receivers_by_claims, total_available_quantity, city_with_most_listings,
    most_common_food_types, claims_per_food_item, provider_with_most_completed_claims,
    claims_percentage_by_status, avg_quantity_claimed_per_receiver, most_claimed_meal_type,
    total_quantity_by_provider, near_expiry_items, claim_completion_rate_over_time
)

st.set_page_config(page_title='SQL Queries', layout='wide')
st.title('🔍 SQL Query Outputs')

st.subheader('1) Providers & Receivers by City')
st.dataframe(providers_receivers_by_city())

st.subheader('2) Provider Types contributing the most')
st.dataframe(top_provider_types())

st.subheader('3) Provider contacts by city')
city = st.text_input('City for contacts', '')
if city:
    st.dataframe(provider_contacts_by_city(city))

st.subheader('4) Receivers with most claims')
st.dataframe(top_receivers_by_claims())

st.subheader('5) Total available quantity')
st.dataframe(total_available_quantity())

st.subheader('6) City with most listings')
st.dataframe(city_with_most_listings())

st.subheader('7) Most common food types')
st.dataframe(most_common_food_types())

st.subheader('8) Claims per food item')
st.dataframe(claims_per_food_item())

st.subheader('9) Provider with highest completed claims')
st.dataframe(provider_with_most_completed_claims())

st.subheader('10) Claims by status (%)')
st.dataframe(claims_percentage_by_status())

st.subheader('11) Avg quantity claimed per receiver')
st.dataframe(avg_quantity_claimed_per_receiver())

st.subheader('12) Most claimed meal type')
st.dataframe(most_claimed_meal_type())

st.subheader('13) Total quantity donated by provider')
st.dataframe(total_quantity_by_provider())

st.subheader('14) Near-expiry items (<=2 days from today)')
today = st.date_input('Today', help='Used to find items expiring in next 2 days')
if today:
    st.dataframe(near_expiry_items(today.isoformat()))

st.subheader('15) Claim completion rate over time (YYYY-MM)')
st.dataframe(claim_completion_rate_over_time())
