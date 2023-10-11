
#######################################################################################################################################
### import libraries
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_distances


#######################################################################################################################################
### Set page layout into wide mode
st.set_page_config(
    page_title="Adventure Playlist",
    layout="wide"
)

### Create a title
st.title("Adventure")


#######################################################################################################################################
### Preprocessed data loading

# preprocessed dataframe for all tracks in the database
df_track_vec = pd.read_csv("data/df_track_vec.csv")

# preprocessed dataframe for tracks in the user's listening history
df_user_unsorted = pd.read_csv("data/df_user_a.csv")
df_user = df_user_unsorted.sort_values(by=['playcount'], ascending=False).reset_index(drop=True)


#######################################################################################################################################
### Recommendation function

def nr_rec(df_track_vec, df_user, alpha=0.5):

    '''
    makes a playlist of top 10 recommendations using content-based novelty-relevance approach with the 7 audio 
    features 'danceability', 'energy', 'speechiness', 'instrumentalness', 'liveness', 'valence', 'tempo_scaled'
    
    Inputs
    ---------------
    df_track_vec: a pre-processed dataframe containing all tracks in the database with all basic information,
                  audio features, and count-vectorized columns of tags of the tracks
    df_user: a pre-processed dataframe containing all tracks in the user's listening history with all basic
             information, audio features and count-vectorized columns of tags of the tracks
    
    Outputs
    ---------------
    returns a dataframe listing the top 10 recommendations with track_id, track name, artist name, spotify preview url,
    year, tags, and the novelty-relevance scores
    
    '''
    
    assert isinstance(alpha, (float, int)), 'alpha must be a number'
    assert (alpha >= 0.0) & (alpha <= 1.0), 'alpha must be between 0.0 and 1.0'
    
    # creating a dataframe of all tracks in the database for comparing Novelty-Relevance score
    df_nr_rec = df_track_vec[['track_id', 'name', 'artist', 'spotify_preview_url', 'year', 'tags']].copy()

    # Relevance score
    df_tag_track = df_track_vec.iloc[:,21:]
    df_tag_user = df_user.iloc[:,23:]
    relevance_mat = pairwise_distances(df_tag_track, df_tag_user, metric='cosine')
    avg_relevance_mat = relevance_mat.mean(axis=1)
    df_nr_rec['relevance'] = avg_relevance_mat

    # Novelty score
    attribute_list = ['danceability', 'energy', 'speechiness', 'instrumentalness', 'liveness', 'valence', 'tempo_scaled']

    df_af_track = df_track_vec[attribute_list]
    df_af_user = df_user[attribute_list]
    novelty_mat = cosine_distances(df_af_track, df_af_user) / 2
    avg_novelty_mat = novelty_mat.mean(axis=1)
    df_nr_rec['novelty'] = avg_novelty_mat

    # Novelty-Relevance score
    df_nr_rec['nr_score'] = alpha * df_nr_rec['novelty'] + (1-alpha) * df_nr_rec['relevance']

    # Playlist of top 10 recommendations by Novelty-Relevance score
    df_nr_rec_top10 = df_nr_rec.sort_values(by=['nr_score'], ascending=False).reset_index(drop=True)[:10]

    # returning the results
    return df_nr_rec_top10



col1, col2 = st.columns(2)

### column 1 shows the slider and the recommendations
with col1:
    ### slider version, alpha value from slider
    st.subheader("Feel free to customize the :notes: Novelty :notes: of your playlist!")
    alpha = float(st.slider(" ", min_value=0.0, max_value=1.0, value=0.5))
    st.write("Novelty:", alpha)

    ### Make recommendations

    df_nr_rec_top10 = nr_rec(df_track_vec, df_user, alpha=alpha)

    st.write(" ")
    df_nr_rec_top10_playlist = df_nr_rec_top10[['name', 'artist', 'year', 'tags']]
    st.dataframe(df_nr_rec_top10_playlist, use_container_width=True)

### column 2 shows the 10 recommended tracks with audio players
with col2:
    st.subheader("Let's play it!")
    for i in range(10):
        st.table(df_nr_rec_top10_playlist[i:i+1])
        st.audio(df_nr_rec_top10.loc[i]['spotify_preview_url'], format='audio/mp3')
        st.write(" ")

st.divider()

#######################################################################################################################################
### User's listening history

df_user_playlist = df_user[['playcount', 'name', 'artist', 'year', 'tags']]

st.title("Your Listening History")
st.write(" ")


col1, col2 = st.columns(2)

### column 1 shows the top 10 most played tracks from the user's listening history
with col1:
    st.dataframe(df_user_playlist.head(10), use_container_width=True)

### column 2 shows those tracks with audio players
with col2:
    for i in range(df_user_playlist.shape[0]):
        st.table(df_user_playlist[i:i+1])
        st.audio(df_user.loc[i]['spotify_preview_url'], format='audio/mp3')
        st.write(" ")

#######################################################################################################################################
