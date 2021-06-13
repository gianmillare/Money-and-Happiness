import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt

DATA_URL = ("resources/cfwb.csv")

st.title("Does Money equal happiness?")
st.markdown("### An overview data analysis on life satisfaction and financial well-being!")

@st.cache(persist=True)
def load_data():
    original_data = pd.read_csv(DATA_URL)
    data = original_data[['SWB_1', 'FWBscore', 'ENDSMEET', 'FSscore', 'LMscore']]
    return data

data = load_data()

# Overview
