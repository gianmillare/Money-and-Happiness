import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt

DATA_URL = ("resources/cfwb.csv")

st.title("Does money equal happiness?")
st.markdown("### An overview data analysis on life satisfaction and financial well-being!")
st.text("Approximately 6,400 people were surveyed on their overall satisfaction with life and \ntheir financial statuses."
        " In this project, I attempt to define the correlation between \nfinancial capabilities and happiness.")

@st.cache(persist=True)
def load_data():
    original_data = pd.read_csv(DATA_URL)
    data = original_data[['SWB_1', 'FWBscore', 'ENDSMEET', 'FSscore', 'LMscore']]
    return data

data = load_data()

st.text('---------------------------------------------------------------------------------')

# Overview
st.markdown('### Overview: What is the general satisfaction across the sample?')
satisfaction_ratings = data['SWB_1'].value_counts().to_dict()
satisfaction_ratings = {str(key): value for key, value in satisfaction_ratings.items()}

labels = ' ', ' ', 'Slightly Disagree', 'Neutral', 'Slightly Agree', 'Agree', 'Strongly Agree'
sizes = [satisfaction_ratings['1'], satisfaction_ratings['2'], satisfaction_ratings['3'],
        satisfaction_ratings['4'], satisfaction_ratings['5'], satisfaction_ratings['6'], satisfaction_ratings['7']]
explode = (0,0,0,0,0,0.15,0)
colors = ['bisque','burlywood','goldenrod','limegreen','slategray','skyblue','royalblue']

fig, ax = plt.subplots(figsize =(20, 15))
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
ax.set_title('"I am satisfied with life"', fontsize=35,fontweight='bold')
ax.axis('equal')

plt.rcParams.update({'font.size': 22})
plt.tight_layout()
plt.show()
st.pyplot(fig)

st.markdown("Thankfully, it seems that most people (~77%) in this sample are at least slightly satisfied with life.")
st.text('---------------------------------------------------------------------------------')