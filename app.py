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

# Question 1: Are financially responsbile people more satisfied with life?
st.markdown("### Are financially stable people more satisfied with life?")
st.text("In this section, I divide people with life satisfaction ratings 5+ from people <=3. Then I \nlook at how they rate their financial stability.")
st.text(" The Financial Well-Being score for each respondent was based on the score (1-4) given to \nquestions like:"
        "\n- I could handle a major unexpected expense"
        "\n- I can enjoy life because of the way I’m managing my money"
        "\n- I am concerned that the money I have or will save won’t last"
        "\n- etc.")
st.text(" The Financial skill score for each respondent was based on the score (1-5) given to \nquestions like:"
        "\n- I know how to make complex financial decisions"
        "\n- I am able to recognize a good financial investment"
        "\n- I know how to keep myself from spending too much"
        "\n- etc.")

average_fwb_1 = data.loc[data['SWB_1'] == 1]['FWBscore'].mean()
average_fwb_2 = data.loc[data['SWB_1'] == 2]['FWBscore'].mean()
average_fwb_3 = data.loc[data['SWB_1'] == 3]['FWBscore'].mean()
average_fwb_5 = data.loc[data['SWB_1'] == 5]['FWBscore'].mean()
average_fwb_6 = data.loc[data['SWB_1'] == 6]['FWBscore'].mean()
average_fwb_7 = data.loc[data['SWB_1'] == 7]['FWBscore'].mean()
fwb_scores = [average_fwb_1, average_fwb_2, average_fwb_3, average_fwb_5, average_fwb_6, average_fwb_7]
print(fwb_scores)

fs_score_1 = data.loc[data['SWB_1'] == 1]['FSscore'].mean()
fs_score_2 = data.loc[data['SWB_1'] == 2]['FSscore'].mean()
fs_score_3 = data.loc[data['SWB_1'] == 3]['FSscore'].mean()
fs_score_5 = data.loc[data['SWB_1'] == 5]['FSscore'].mean()
fs_score_6 = data.loc[data['SWB_1'] == 6]['FSscore'].mean()
fs_score_7 = data.loc[data['SWB_1'] == 7]['FSscore'].mean()
fs_scores = [fs_score_1, fs_score_2, fs_score_3, fs_score_5, fs_score_6, fs_score_7]
print(fs_scores)

lm_score_1 = data.loc[data['SWB_1'] == 1]['LMscore'].mean()
lm_score_2 = data.loc[data['SWB_1'] == 2]['LMscore'].mean()
lm_score_3 = data.loc[data['SWB_1'] == 3]['LMscore'].mean()
lm_score_5 = data.loc[data['SWB_1'] == 5]['LMscore'].mean()
lm_score_6 = data.loc[data['SWB_1'] == 6]['LMscore'].mean()
lm_score_7 = data.loc[data['SWB_1'] == 7]['LMscore'].mean()
lm_scores = [lm_score_1, lm_score_2, lm_score_3, lm_score_5, lm_score_6, lm_score_7]
print(lm_scores)

labels = ['Strongly Unsatisfied', 'Unsatisfied', 'Slightly Unsatisfied', 'Slightly Satisfied', 
          'Satisfied', 'Strongly Satisfied']

# x = fwb_scores, fs_scores

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig2, ax = plt.subplots(figsize=(15,10))
rects1 = ax.bar(x - width/2, fwb_scores, width, label='Financial Well-Being', color='skyblue')
rects2 = ax.bar(x + width/2, fs_scores, width, label='Financial Skill', color='gray')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Scores\n', fontsize=15)
ax.set_title('Average Scores by Life Satisfaction', fontsize=25)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=15)
ax.legend(fontsize=15)
ax.set_facecolor('whitesmoke')
plt.grid(color='slategrey', linestyle='--')

plt.show()
st.pyplot(fig2)

st.text("According to the chart above, as the average financial well-being and Financial Skills \nscore increased, the life-satisfaction rating also increased."
        " In other words, people who \nwere more financially stable and financially conscious were happier with their lives.")

st.text('---------------------------------------------------------------------------------')

# Question 2: Are financially literate/educated people more satisfied with life?
st.markdown("### Are financially literate/educated people more satisfied with life?")
st.text("It is one thing to be financially conscious and responsible, but nowadays, to reach \nfinancial freedom, a level of financial education may be required.")
st.text("A common test of financial education is the Lusardi Mitchell Financial Literacy Test. \nThis survey recorded responses to that test.")

labels = ['Strongly Unsatisfied', 'Unsatisfied', 'Slightly Unsatisfied', 'Slightly Satisfied', 
          'Satisfied', 'Strongly Satisfied']
# lm_scores
fig3, ax = plt.subplots(figsize=(15, 12))

ax.set_yticklabels(labels, fontsize=15)
ax.set_title("Lusardi and Mitchell Financial Literacy Score", fontsize=25)
plt.barh(labels, lm_scores, color='skyblue')
plt.grid(color='slategrey', linestyle='--', axis='x')

for i, j in enumerate(lm_scores):
    plt.text(j,i, " " + str(round(j, 2)), fontsize=15)
    
plt.show()
st.pyplot(fig3)

st.text("According to the chart above, there is no significant disparity between unsatisfied and \nsatisfied respondents to their financial skill.")