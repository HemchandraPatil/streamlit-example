# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import sum, col
import altair as alt

# Set page config
st.set_page_config(layout="wide")
st.title("Welcome to Streamlit in Snowflake")
st.header("Saama Thunder's") 
