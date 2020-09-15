'''
This script performs topic modeling on each of the 5 clusters.
'''

import pandas as pd

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF

from nltk import word_tokenize
from nltk import pos_tag

def create_dataframes_for_clusters(updated_text_df):
    '''
    A function that takes in a dataframe with clusters and returns 5 dataframes:
    one for each unique cluster.

    Parameters
    ----------
    updated_text_df : A clean text dataframe that has the clusters appended

    Returns
    -------
    A dataframe for each cluster of diarist (5 in total).
    '''

    # cluster 0
    cluster_0 = updated_text_df[updated_text_df['Cluster'] == 0]
    del cluster_0['Cluster']

    # cluster 1
    cluster_1 = updated_text_df[updated_text_df['Cluster'] == 1]
    del cluster_1['Cluster']

    # cluster 2
    cluster_2 = updated_text_df[updated_text_df['Cluster'] == 2]
    del cluster_2['Cluster']

    # cluster 3
    cluster_3 = updated_text_df[updated_text_df['Cluster'] == 3]
    del cluster_3['Cluster']

    # cluster 4
    cluster_4 = updated_text_df[updated_text_df['Cluster'] == 4]
    del cluster_4['Cluster']

    return cluster_0, cluster_1, cluster_2, cluster_3, cluster_4

def display_topics(model, feature_names, no_top_words, topic_names=None):
    '''
    Given a model, return the top words for each topic.

    Parameters
    ----------
    model : A NMF, LSA, or LDA model of text data.
    feature_names : A list of features extracted from the vectorized model.
    no_top_words : The number of top wrods to display from each topic.
    topic_names : The names of the topics. Set to None as default.

    Returns
    -------
    The top words for each topic.
    '''
    for i, topic in enumerate(model.components_):
        if not topic_names or not topic_names[i]:
            print("\nTopic ", i)
        else:
            print("\nTopic: '", topic_names[i], "'")
        print(", ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

def nouns(text_string):
    '''
    Given a string of text, tokenize the text and pull out only the nouns.

    Parameters
    ----------
    text_string : A string of text.

    Returns
    -------
    A tokenized version of the text only containing nouns.
    '''
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = word_tokenize(text_string)
    all_nouns = [word for (word, pos) in pos_tag(tokenized) if is_noun(pos)]
    return ' '.join(all_nouns)

def new_stopwords():
    '''
    Returns a list of of stop words that joins a custom list with the
    standard English stop words.

    Parameters
    ----------

    Returns
    -------
    An updated list of stop words that has been appended to the stop words provided
    by the model.
    '''
    additional_stop_words = ['pm', 'im', 'day', 'week', 'total', 'daily', 'like',
                             'today', 'dont', 'just', 'women', 'way', 'really',
                             'ive', 'diaries', 'got', 'gets', 'ill', 'things',
                             'bit', 'sevenday', 'hes', 'let', 'shes', 'lot',
                             'little', 'decide', 'ready', 'feel', 'goes', 'stop',
                             'finally', 'welcome', 'money', 'diaries', 'period',
                             'job', 'share', 'today', 'millennials', 'occupation',
                             'paycheck', 'diaries', 'taboo', 'dollar', 'period',
                             'year', 'month', 'worth', 'rent', 'bonus', 'expenses',
                             'today', 'mortgage', 'debt', 'expensesmortgage',
                             'industry', 'expensesrent', 'salary', 'savings',
                             'insurance', 'loan', 'loans', 'income', 'student',
                             'dollartoday', 'cash', 'room', 'account', 'woman',
                             'living', 'house', 'housing', 'mortgagepaycheck',
                             'half', 'split', 'apartment', 'totaldebt', 'checksavingscd',
                             'stuff', 'hour', 'hours', 'people', 'place', 'years',
                             'minutes', 'tomorrow', 'couple', 'head', 'meeting']

    stop_words = text.ENGLISH_STOP_WORDS.union(additional_stop_words)

    return stop_words

def create_noun_dataframe(data_clean):
    '''
    A function that takes in a dataframe and returns a new dataframe that has been applied
    with the nouns function.

    Parameters
    ----------
    data_clean : A dataframe where all of the text has been cleaned.

    Returns
    -------
    A new dataframe containing only nouns in the text.
    '''
    data_nouns = pd.DataFrame(data_clean.diary_text_string.apply(nouns))
    return data_nouns

def topic_modeling(data_nouns):
    '''
    Performs topic modeling using count vectorizer, noun parts-of-speech tagging,
    non-negative matrix factorization, a custom list of stop words, and 5 topics.
    Return 3 items that should be pickled for each cluster to be used later for the app.

    Parameters
    ----------
    data_nouns : A clean text dataframe where the text only contains nouns.

    Returns
    -------
    The count vectorizer, NMF model, and NMF that should be pickled to be later used
    to create the recommender app.
    '''
    stop_words = new_stopwords()

    # use count vectorizer
    cvn = CountVectorizer(stop_words=stop_words, min_df=0.1, max_df=.9, ngram_range=(1, 2))
    data_cvn = cvn.fit_transform(data_nouns.diary_text_string)
    data_dtmn = pd.DataFrame(data_cvn.toarray(), columns=cvn.get_feature_names())
    data_dtmn.index = data_nouns.index

    # create NMF object and transform the document term object created above
    nmf = NMF(5, random_state=19)

    # View top words in each topic
    display_topics(nmf, cvn.get_feature_names(), 10)

def main():
    '''
    Loads in the cleaned diary text dataframe, calls NMF noun topic modeling, and
    returns top topics, a document term matrix and a term document matrix.
    '''

    # Load in csv files
    text_df = pd.read_csv('text_df.csv')
    clustered_data_scaled = pd.read_csv('clustered_data_scaled.csv')

    # Merge datasets together
    updated_text_df = pd.merge(clustered_data_scaled, text_df, left_on='story_title',
                               right_on='story_title')

    # Create dataframes for each cluster
    cluster_0, cluster_1, cluster_2, cluster_3, cluster_4 = create_dataframes_for_clusters(
        updated_text_df)

    # Cluster 0 topic modeling
    data_nouns_cluster_0 = create_noun_dataframe(cluster_0)
    topic_modeling(data_nouns_cluster_0)

    # Cluster 1 topic modeling
    data_nouns_cluster_1 = create_noun_dataframe(cluster_1)
    topic_modeling(data_nouns_cluster_1)

    # Cluster 2 topic modeling
    data_nouns_cluster_2 = create_noun_dataframe(cluster_2)
    topic_modeling(data_nouns_cluster_2)

    # Cluster 3 topic modeling
    data_nouns_cluster_3 = create_noun_dataframe(cluster_3)
    topic_modeling(data_nouns_cluster_3)

    # Cluster 4 topic modeling
    data_nouns_cluster_4 = create_noun_dataframe(cluster_4)
    topic_modeling(data_nouns_cluster_4)

main()
