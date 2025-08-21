import streamlit as st
from utils.filters import get_filter_options, filtered_food_listings
from utils.query_functions import total_available_quantity

st.set_page_config(page_title='Local Food Wastage Management System', layout='wide')

st.title('Local Food Wastage Management System')

st.write('Filter the available food by city, provider type, food type, and meal type.')

opts = get_filter_options()

city = st.selectbox('City', [''] + opts['cities'])
ptype = st.selectbox('Provider Type', [''] + opts['provider_types'])
ftype = st.selectbox('Food Type', [''] + opts['food_types'])
mtype = st.selectbox('Meal Type', [''] + opts['meal_types'])

df = filtered_food_listings(city if city else None,
                            ptype if ptype else None,
                            ftype if ftype else None,
                            mtype if mtype else None)

st.subheader('Filtered Food Listings')
st.dataframe(df)

st.markdown('---')
st.subheader('Quick Stat: Total Available Quantity')
st.dataframe(total_available_quantity())
st.info('Navigate to the **Pages** sidebar for EDA and SQL queries.')
