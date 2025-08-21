import pandas as pd
import plotly.express as px

def bar_top_provider_types(df: pd.DataFrame):
    fig = px.bar(df, x='Provider_Type', y='Total_Quantity', title='Top Provider Types by Quantity')
    return fig

def line_claims_over_time(df: pd.DataFrame):
    long_df = df.melt(id_vars=['YearMonth'], value_vars=['Completed','Pending','Cancelled'],
                      var_name='Status', value_name='Count')
    fig = px.line(long_df, x='YearMonth', y='Count', color='Status', title='Claims Over Time by Status')
    return fig

def pie_claims_by_status(df: pd.DataFrame):
    fig = px.pie(df, names='Status', values='Percentage', title='Claims by Status (%)')
    return fig

def bar_food_types(df: pd.DataFrame):
    fig = px.bar(df, x='Food_Type', y='Count', title='Most Common Food Types')
    return fig

def bar_city_listings(df: pd.DataFrame):
    fig = px.bar(df, x='City', y='Listings', title='Listings by City')
    return fig
