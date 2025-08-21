import streamlit as st
import pandas as pd
from utils.query_functions import (
    top_provider_types, claim_completion_rate_over_time, most_common_food_types, city_with_most_listings
)
from utils.visualization import (
    bar_top_provider_types, line_claims_over_time, pie_claims_by_status, bar_food_types, bar_city_listings
)
from utils.query_functions import claims_percentage_by_status

st.set_page_config(page_title='EDA Analysis', layout='wide')

st.title('📊 EDA & Insights')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Top Provider Types by Quantity')
    df_types = top_provider_types()
    st.plotly_chart(bar_top_provider_types(df_types), use_container_width=True)

with col2:
    st.subheader('Most Common Food Types')
    df_food_types = most_common_food_types()
    st.plotly_chart(bar_food_types(df_food_types), use_container_width=True)

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader('Listings by City')
    df_city = city_with_most_listings()
    st.plotly_chart(bar_city_listings(df_city), use_container_width=True)

with col4:
    st.subheader('Claims by Status (%)')
    df_pct = claims_percentage_by_status()
    st.plotly_chart(pie_claims_by_status(df_pct), use_container_width=True)

st.divider()

st.subheader('Claims Over Time by Status')
df_over_time = claim_completion_rate_over_time()
st.plotly_chart(line_claims_over_time(df_over_time), use_container_width=True)
