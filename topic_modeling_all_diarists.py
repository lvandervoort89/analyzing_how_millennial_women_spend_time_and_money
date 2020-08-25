'''
This script performs topic modeling on the text from all diarists.
'''

import pandas as pd

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF

from nltk import word_tokenize
from nltk import pos_tag

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
                             'minutes', 'tomorrow']

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

    Parameters
    ----------
    data_nouns : A clean text dataframe where the text only contains nouns.

    Returns
    -------
    A print out of the top 10 words for each of the topics, the document term matrix,
    and the NMF model applied to the document term matrix.
    '''
    stop_words = new_stopwords()

    # use count vectorizer
    cvn = CountVectorizer(stop_words=stop_words, min_df=0.1, max_df=.9, ngram_range=(1, 2))
    data_cvn = cvn.fit_transform(data_nouns.diary_text_string)
    data_dtmn = pd.DataFrame(data_cvn.toarray(), columns=cvn.get_feature_names())
    data_dtmn.index = data_nouns.index

    # create NMF object and transform the document term object created above
    nmf = NMF(5, random_state=19)
    doc_topic = nmf.fit_transform(data_dtmn)

    # View top words in each topic
    display_topics(nmf, cvn.get_feature_names(), 10)

    return data_dtmn, doc_topic

def term_document_matrix(doc_topic):
    '''
    A function that takes in doc_topic and returns a term document matrix.

    Parameters
    ----------
    doc_topic : The NMF model that's been applied to the document term matrix.

    Returns
    -------
    A term document matrix that shows the diarists and how each diary is made
    up of the 8 topics.
    '''
    term_doc_matrix = pd.DataFrame(doc_topic.round(5), columns=[
        'component_1', 'component_2', 'component_3', 'component_4',
        'compnent_5', 'component_6', 'component_7', 'component_8'])

    return term_doc_matrix
