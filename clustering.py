'''
This script performs clustering on the diaries metadata.
'''

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster_metadata(diarist_df_numerical):
    '''
    A function that takes a numerical dataframe containing age and salary and
    creates 5 clusters (optimized by elbow method graph).

    Parameters
    ----------
    diarist_df_numerical : A cleaned dataframe containing the age and salary
    metadata for each diarist.

    Returns
    -------
    kfit : The kmeans model that has been fit to the scaled data.
    diarist_df_scaled : The diarist_df that has been scaled.
    identified_clusters_scaled : The clusters for each diarist that has been scaled.
    '''
    # scale features
    scaler = StandardScaler()
    columns_scaled = scaler.fit_transform(diarist_df_numerical.values)
    diarist_df_scaled = pd.DataFrame(columns_scaled, columns=diarist_df_numerical.columns)

    # Modeling
    kmeans = KMeans(n_clusters=5, random_state=20)
    kfit = kmeans.fit(diarist_df_scaled)
    identified_clusters_scaled = kfit.predict(diarist_df_scaled)

    return kfit, diarist_df_scaled, identified_clusters_scaled

def append_clusters_to_df(diarist_df, scaled_clusters):
    '''
    A function that takes the diarist dataframe and list of clusters and appends
    the clusters to the dataframe.

    Parameters
    ----------
    diarist_df : The cleaned diarist metadata dataframe.
    scaled_clusters : The list of scaled clusters for each diarist.

    Returns
    -------
    A dataframe that has the clusters appended to it.
    '''
    clustered_data_scaled = diarist_df.copy()
    clustered_data_scaled['Cluster'] = scaled_clusters

    return clustered_data_scaled
