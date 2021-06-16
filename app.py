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

fig1, ax = plt.subplots(figsize =(20, 15))
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
ax.set_title('"I am satisfied with life"', fontsize=35,fontweight='bold')
ax.axis('equal')

plt.rcParams.update({'font.size': 30})
plt.tight_layout()
plt.show()
st.pyplot(fig1)

st.markdown("Thankfully, it seems that most people (~77%) in this sample are at least slightly satisfied with life.")
st.text('---------------------------------------------------------------------------------')

# Question 1: Are financially stable people more satisfied with life?
st.markdown("### Are financially stable people more satisfied with life?")
st.text("In this section, I divide people with life satisfaction ratings 5+ from people <=3. Then I \nlook at how they rate their financial stability."
        " The Financial Well-Being score for each \nrespondent was based on the score (1-4) given to questions like:"
        "\n- I could handle a major unexpected expense"
        "\n- I can enjoy life because of the way I’m managing my money"
        "\n- I am concerned that the money I have or will save won’t last"
        "\n- etc.")

# Strongly Unsatisfied
strongly_unsatisfied = data.loc[data['SWB_1'] == 1]
average_fwb_1 = strongly_unsatisfied['FWBscore'].mean()
# Unsatisfied
unsatisfied = data.loc[data['SWB_1'] == 2]
average_fwb_2 = unsatisfied['FWBscore'].mean()
# Slightly Unsatisfied
slightly_unsatisfied = data.loc[data['SWB_1'] == 3]
average_fwb_3 = slightly_unsatisfied['FWBscore'].mean()
# Slightly Satisfied
slightly_satisfied = data.loc[data['SWB_1'] == 5]
average_fwb_5 = slightly_satisfied['FWBscore'].mean()
# Satisfied
satisfied = data.loc[data['SWB_1'] == 6]
average_fwb_6 = satisfied['FWBscore'].mean()
# Strongly Satisfied
strongly_satisfied = data.loc[data['SWB_1'] == 7]
average_fwb_7 = strongly_satisfied['FWBscore'].mean()

labels = 'Strongly Unsatisfied', 'Unsatisfied', 'Slightly Unsatisfied', 'Slightly Satisfied', 'Satisfied', 'Strongly Satisfied'
average_fwb = [average_fwb_1, average_fwb_2, average_fwb_3, average_fwb_5, average_fwb_6, average_fwb_7]
y_pos = np.arange(len(labels))

fig2, ax = plt.subplots(figsize =(15, 10))

y_pos = np.arange(len(labels))
ax.barh(y_pos, average_fwb, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=15)
ax.set_xlabel('Average FWB Score', fontsize=15)
ax.set_title('Average Financial Well-Being Score by Satisfaction', fontsize=25)
for index, value in enumerate(average_fwb):
    plt.text(value, index,
             " " + str(round(value)), fontweight='bold', fontsize=18)

plt.tick_params(
    axis='x',          
    which='both',      
    bottom=False,      
    top=False,         
    labelbottom=False)
plt.show()

st.pyplot(fig2)

st.text("According to the chart above, as the average financial well-being score increased, the \nlife-satisfaction rating also increased."
        " In other words, people who were more financially \nstable and financially conscious were happier with their lives.")