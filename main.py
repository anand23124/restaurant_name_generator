import streamlit as st
from langchain_helper import get_restaurant_name_and_items
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","Arabic","American"))


if cuisine:
    response = get_restaurant_name_and_items(cuisine)
    
    st.header(response['Restaurant_name'])
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for items in menu_items:
        st.write(items)