import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("HELLO world!!!!")

st.subheader("This is subheader")

Stage_name =st.selectbox("Stage Name: ", 
                          ["STAGE1","STAGE2","STAGE3"])

st.write("You have selected ",Stage_name)
