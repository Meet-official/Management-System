import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import streamlit as st
import pandas as pd
from utils.filters import get_filter_options, filtered_food_listings
from utils.query_functions import run_sql
from utils.db_connection import get_connection
from data.database.crud_operations import (
    add_provider, update_provider, delete_provider,
    add_receiver, update_receiver, delete_receiver,
    add_food_listing, update_food_listing, delete_food_listing,
    add_claim, update_claim, delete_claim
)

st.set_page_config(page_title='CRUD Operations', layout='wide')
st.title('📝 CRUD Operations')

tab1, tab2, tab3, tab4 = st.tabs(['Providers', 'Receivers', 'Food Listings', 'Claims'])

with tab1:
    st.subheader('Add / Update / Delete Provider')
    with st.form('add_provider'):
        col1, col2, col3 = st.columns(3)
        with col1:
            pid = st.number_input('Provider_ID (optional for auto)', min_value=0, step=1)
            name = st.text_input('Name')
        with col2:
            ptype = st.text_input('Type')
            city = st.text_input('City')
        with col3:
            contact = st.text_input('Contact')
            address = st.text_input('Address')
        submitted = st.form_submit_button('Add Provider')
        if submitted and name and ptype and city:
            add_provider({'Provider_ID': pid or None, 'Name': name, 'Type': ptype, 'Address': address, 'City': city, 'Contact': contact})
            st.success('Provider added')
    st.dataframe(run_sql('SELECT * FROM providers ORDER BY Provider_ID'))

    st.markdown('---')
    up_id = st.number_input('Provider_ID to update/delete', min_value=0, step=1, key='p_up')
    new_city = st.text_input('New City')
    if st.button('Update City'):
        update_provider(int(up_id), {'City': new_city})
        st.success('Provider updated')
    if st.button('Delete Provider'):
        delete_provider(int(up_id))
        st.warning('Provider deleted')

with tab2:
    st.subheader('Add / Update / Delete Receiver')
    with st.form('add_receiver'):
        col1, col2, col3 = st.columns(3)
        with col1:
            rid = st.number_input('Receiver_ID (optional for auto)', min_value=0, step=1)
            name = st.text_input('Name', key='rname')
        with col2:
            rtype = st.text_input('Type')
            city = st.text_input('City', key='rcity')
        with col3:
            contact = st.text_input('Contact', key='rcontact')
        submitted = st.form_submit_button('Add Receiver')
        if submitted and name and rtype and city:
            add_receiver({'Receiver_ID': rid or None, 'Name': name, 'Type': rtype, 'City': city, 'Contact': contact})
            st.success('Receiver added')
    st.dataframe(run_sql('SELECT * FROM receivers ORDER BY Receiver_ID'))

    st.markdown('---')
    up_id = st.number_input('Receiver_ID to update/delete', min_value=0, step=1, key='r_up')
    new_city = st.text_input('New City', key='r_new_city')
    if st.button('Update City', key='r_update_btn'):
        update_receiver(int(up_id), {'City': new_city})
        st.success('Receiver updated')
    if st.button('Delete Receiver', key='r_delete_btn'):
        delete_receiver(int(up_id))
        st.warning('Receiver deleted')

with tab3:
    st.subheader('Add / Update / Delete Food Listing')
    with st.form('add_food'):
        col1, col2, col3 = st.columns(3)
        with col1:
            fid = st.number_input('Food_ID (optional for auto)', min_value=0, step=1)
            fname = st.text_input('Food_Name')
            qty = st.number_input('Quantity', min_value=0, step=1)
        with col2:
            exp = st.date_input('Expiry_Date')
            pid = st.number_input('Provider_ID', min_value=0, step=1, key='pid_food')
            ptype = st.text_input('Provider_Type')
        with col3:
            loc = st.text_input('Location')
            ftype = st.text_input('Food_Type')
            mtype = st.text_input('Meal_Type')
        submitted = st.form_submit_button('Add Food Listing')
        if submitted and fname and ptype and loc and ftype and mtype:
            add_food_listing({'Food_ID': fid or None, 'Food_Name': fname, 'Quantity': int(qty),
                              'Expiry_Date': exp.isoformat(), 'Provider_ID': int(pid),
                              'Provider_Type': ptype, 'Location': loc, 'Food_Type': ftype,
                              'Meal_Type': mtype, 'Status': 'Available'})
            st.success('Food listing added')
    st.dataframe(run_sql('SELECT * FROM food_listings ORDER BY Food_ID'))

    st.markdown('---')
    up_id = st.number_input('Food_ID to update/delete', min_value=0, step=1, key='f_up')
    new_status = st.selectbox('New Status', ['Available','Claimed','Expired'])
    if st.button('Update Status'):
        update_food_listing(int(up_id), {'Status': new_status})
        st.success('Food listing updated')
    if st.button('Delete Food Listing'):
        delete_food_listing(int(up_id))
        st.warning('Food listing deleted')

with tab4:
    st.subheader('Add / Update / Delete Claim')
    with st.form('add_claim'):
        col1, col2, col3 = st.columns(3)
        with col1:
            cid = st.number_input('Claim_ID (optional for auto)', min_value=0, step=1)
            fid = st.number_input('Food_ID', min_value=0, step=1, key='c_food')
        with col2:
            rid = st.number_input('Receiver_ID', min_value=0, step=1, key='c_receiver')
            status = st.selectbox('Status', ['Pending','Completed','Cancelled'])
        with col3:
            ts = st.text_input('Timestamp (YYYY-MM-DD HH:MM:SS)')
        submitted = st.form_submit_button('Add Claim')
        if submitted and fid and rid and status and ts:
            add_claim({'Claim_ID': cid or None, 'Food_ID': int(fid), 'Receiver_ID': int(rid), 'Status': status, 'Timestamp': ts})
            st.success('Claim added')
    st.dataframe(run_sql('SELECT * FROM claims ORDER BY Claim_ID'))

    st.markdown('---')
    up_id = st.number_input('Claim_ID to update/delete', min_value=0, step=1, key='c_up')
    new_status = st.selectbox('New Status', ['Pending','Completed','Cancelled'], key='c_status2')
    if st.button('Update Claim'):
        update_claim(int(up_id), {'Status': new_status})
        st.success('Claim updated')
    if st.button('Delete Claim'):
        delete_claim(int(up_id))
        st.warning('Claim deleted')
