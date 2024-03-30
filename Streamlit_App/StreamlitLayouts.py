import streamlit as st

st.set_page_config(page_title= "this is config page title" , layout='wide')
st.title("Streamlit Layouts")

#Side Bar
sidebar = st.sidebar
sidebar.write("This is the sidebar")
sidebar.header('Header in Sidebar')

#Columns
# Display image in column layout
col1 , col2 , col3 = st.columns(3)
with col1:
    st.image("./assets/AI.png")

with col2:
    st.image("./assets/About.png")


col1 , col2  = st.columns(2)
with col1:
    st.write("This is Column 1")
    st.image("./assets/AI.png")

with col2:
    st.write("This is Column 2")
    st.image("./assets/About.png")


# Tabs
st.header("Lets create 3 tabs")

tab1 ,tab2 , tab3 = st.tabs(['Tab 1' , 'Tab 2' , 'Tab 3'])
with tab1:
    st.warning("this is my tab dont touch")
    st.image('./assets/About.png')





