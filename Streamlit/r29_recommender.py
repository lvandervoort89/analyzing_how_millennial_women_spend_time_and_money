'''
This script contains code for a Streamlit app to recommend Refinery29 money
Diaries that are similar to the user. The user inputs their age, salary, and a
mini diary of the previous day. The app uses a pickled clustering model to cluster
the user to the original money diaries and then performs cosine similarity to
recommend the 3 diaries most similar to the user's mini diary.
'''

import streamlit as st
import streamlit.components.v1 as components
from joblib import load

import numpy as np

from sklearn.metrics import pairwise_distances


st.title('Refinery29 Money Diary Recommender')
st.subheader(
    'Input some information about yourself and I\'ll recommend a'
    ' few money diaries of people similar to you!'
)

st.text('')

st.markdown(
    'This recommender was created using Natural Language Processing (NLP),'
    ' Non-Negative Matrix Factorization (NMF), K-means clustering, and cosine'
    ' similarity.'
)

st.text('')

age = st.number_input('Age', min_value=20, max_value=100, value=25)
salary = st.number_input('Salary', min_value=20000, max_value=600000, value=50000)

user_diary = [st.text_area('Write a mini diary (paragraph) about what you did yesterday.')]

# predict cluster
scaler = load('scaler.pkl')
kfit = load('kfit.pkl')
new_observation = np.array([age, salary])
new_observation_scaled = scaler.transform(new_observation.reshape(1, -1))

# save predicted cluster
new_observation_cluster = int(kfit.predict(new_observation_scaled))

# topic model with clusters
if new_observation_cluster == 0:
    cvn0 = load('cvn0.pkl')
    doc_topic0 = load('doc_topic0.pkl')
    nmf_model_cluster_0 = load('nmf_model_cluster_0.pkl')
    cluster_0 = load('cluster_0.pkl')
    vector_diary_0 = cvn0.transform(user_diary)
    tranformed_text_0 = nmf_model_cluster_0.transform(vector_diary_0)
    diary_0_rec_array = pairwise_distances(tranformed_text_0, doc_topic0, metric='cosine').argsort()
    diary_0_rec_1 = diary_0_rec_array[0, 0]
    diary_0_rec_2 = diary_0_rec_array[0, 1]
    diary_0_rec_3 = diary_0_rec_array[0, 2]
    diary_0_link_1 = cluster_0.iloc[diary_0_rec_1, 0]
    diary_0_link_2 = cluster_0.iloc[diary_0_rec_2, 0]
    diary_0_link_3 = cluster_0.iloc[diary_0_rec_3, 0]
    diary_0_url_rec1 = 'https://www.refinery29.com' + diary_0_link_1
    diary_0_url_rec2 = 'https://www.refinery29.com' + diary_0_link_2
    diary_0_url_rec3 = 'https://www.refinery29.com' + diary_0_link_3
    if st.button('Recommendation #1'):
        components.iframe(diary_0_url_rec1, height=600, scrolling=True)
    if st.button('Recommendation #2'):
        components.iframe(diary_0_url_rec2, height=600, scrolling=True)
    if st.button('Recommendation #3'):
        components.iframe(diary_0_url_rec3, height=600, scrolling=True)

if new_observation_cluster == 1:
    cvn1 = load('cvn1.pkl')
    doc_topic1 = load('doc_topic1.pkl')
    nmf_model_cluster_1 = load('nmf_model_cluster_1.pkl')
    cluster_1 = load('cluster_1.pkl')
    vector_diary_1 = cvn1.transform(user_diary)
    tranformed_text_1 = nmf_model_cluster_1.transform(vector_diary_1)
    diary_1_rec_array = pairwise_distances(tranformed_text_1, doc_topic1, metric='cosine').argsort()
    diary_1_rec_1 = diary_1_rec_array[0, 0]
    diary_1_rec_2 = diary_1_rec_array[0, 1]
    diary_1_rec_3 = diary_1_rec_array[0, 2]
    diary_1_link_1 = cluster_1.iloc[diary_1_rec_1, 0]
    diary_1_link_2 = cluster_1.iloc[diary_1_rec_2, 0]
    diary_1_link_3 = cluster_1.iloc[diary_1_rec_3, 0]
    diary_1_url_rec1 = 'https://www.refinery29.com' + diary_1_link_1
    diary_1_url_rec2 = 'https://www.refinery29.com' + diary_1_link_2
    diary_1_url_rec3 = 'https://www.refinery29.com' + diary_1_link_3
    if st.button('Recommendation #1'):
        components.iframe(diary_1_url_rec1, height=600, scrolling=True)
    if st.button('Recommendation #2'):
        components.iframe(diary_1_url_rec2, height=600, scrolling=True)
    if st.button('Recommendation #3'):
        components.iframe(diary_1_url_rec3, height=600, scrolling=True)

if new_observation_cluster == 2:
    cvn2 = load('cvn2.pkl')
    doc_topic2 = load('doc_topic2.pkl')
    nmf_model_cluster_2 = load('nmf_model_cluster_2.pkl')
    cluster_2 = load('cluster_2.pkl')
    vector_diary_2 = cvn2.transform(user_diary)
    tranformed_text_2 = nmf_model_cluster_2.transform(vector_diary_2)
    diary_2_rec_array = pairwise_distances(tranformed_text_2, doc_topic2, metric='cosine').argsort()
    diary_2_rec_1 = diary_2_rec_array[0, 0]
    diary_2_rec_2 = diary_2_rec_array[0, 1]
    diary_2_rec_3 = diary_2_rec_array[0, 2]
    diary_2_link_1 = cluster_2.iloc[diary_2_rec_1, 0]
    diary_2_link_2 = cluster_2.iloc[diary_2_rec_2, 0]
    diary_2_link_3 = cluster_2.iloc[diary_2_rec_3, 0]
    diary_2_url_rec1 = 'https://www.refinery29.com' + diary_2_link_1
    diary_2_url_rec2 = 'https://www.refinery29.com' + diary_2_link_2
    diary_2_url_rec3 = 'https://www.refinery29.com' + diary_2_link_3
    if st.button('Recommendation #1'):
        components.iframe(diary_2_url_rec1, height=600, scrolling=True)
    if st.button('Recommendation #2'):
        components.iframe(diary_2_url_rec2, height=600, scrolling=True)
    if st.button('Recommendation #3'):
        components.iframe(diary_2_url_rec3, height=600, scrolling=True)

if new_observation_cluster == 3:
    cvn3 = load('cvn3.pkl')
    doc_topic3 = load('doc_topic3.pkl')
    nmf_model_cluster_3 = load('nmf_model_cluster_3.pkl')
    cluster_3 = load('cluster_3.pkl')
    vector_diary_3 = cvn3.transform(user_diary)
    tranformed_text_3 = nmf_model_cluster_3.transform(vector_diary_3)
    diary_3_rec_array = pairwise_distances(tranformed_text_3, doc_topic3, metric='cosine').argsort()
    diary_3_rec_1 = diary_3_rec_array[0, 0]
    diary_3_rec_2 = diary_3_rec_array[0, 1]
    diary_3_rec_3 = diary_3_rec_array[0, 2]
    diary_3_link_1 = cluster_3.iloc[diary_3_rec_1, 0]
    diary_3_link_2 = cluster_3.iloc[diary_3_rec_2, 0]
    diary_3_link_3 = cluster_3.iloc[diary_3_rec_3, 0]
    diary_3_url_rec1 = 'https://www.refinery29.com' + diary_3_link_1
    diary_3_url_rec2 = 'https://www.refinery29.com' + diary_3_link_2
    diary_3_url_rec3 = 'https://www.refinery29.com' + diary_3_link_3
    if st.button('Recommendation #1'):
        components.iframe(diary_3_url_rec1, height=600, scrolling=True)
    if st.button('Recommendation #2'):
        components.iframe(diary_3_url_rec2, height=600, scrolling=True)
    if st.button('Recommendation #3'):
        components.iframe(diary_3_url_rec3, height=600, scrolling=True)

if new_observation_cluster == 4:
    cvn4 = load('cvn4.pkl')
    doc_topic4 = load('doc_topic4.pkl')
    nmf_model_cluster_4 = load('nmf_model_cluster_4.pkl')
    cluster_4 = load('cluster_4.pkl')
    vector_diary_4 = cvn4.transform(user_diary)
    tranformed_text_4 = nmf_model_cluster_4.transform(vector_diary_4)
    diary_4_rec_array = pairwise_distances(tranformed_text_4, doc_topic4, metric='cosine').argsort()
    diary_4_rec_1 = diary_4_rec_array[0, 0]
    diary_4_rec_2 = diary_4_rec_array[0, 1]
    diary_4_rec_3 = diary_4_rec_array[0, 2]
    diary_4_link_1 = cluster_4.iloc[diary_4_rec_1, 0]
    diary_4_link_2 = cluster_4.iloc[diary_4_rec_2, 0]
    diary_4_link_3 = cluster_4.iloc[diary_4_rec_3, 0]
    diary_4_url_rec1 = 'https://www.refinery29.com' + diary_4_link_1
    diary_4_url_rec2 = 'https://www.refinery29.com' + diary_4_link_2
    diary_4_url_rec3 = 'https://www.refinery29.com' + diary_4_link_3
    if st.button('Recommendation #1'):
        components.iframe(diary_4_url_rec1, height=600, scrolling=True)
    if st.button('Recommendation #2'):
        components.iframe(diary_4_url_rec2, height=600, scrolling=True)
    if st.button('Recommendation #3'):
        components.iframe(diary_4_url_rec3, height=600, scrolling=True)

st.text('')
st.text('')
st.markdown(
    'My name is Lisa VanderVoort, I love reading Refinery29 Money Diaries, and'
    ' working on data science projects. You can read more about my projects'
    ' [here](https://lvandervoort89.github.io) and find my project code'
    ' [here.](https://github.com/lvandervoort89/analyzing_how_millennial_women_spend_time_and_money)'
)
