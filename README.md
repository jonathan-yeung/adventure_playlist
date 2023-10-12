## "Adventure" Playlist - Music Recommendations For Variety And The Long Tail
=========================

The prototype demonstrated as a web app using Streamlit can be found at:
https://adventureplaylist-ggka2gasbwumfp6puzsthw.streamlit.app/

Demo presentation slides of the prototype can be found at:
https://www.canva.com/design/DAFwy7Bk07A/7MNRILwPNCGKtO6VNSEyPg/edit?utm_content=DAFwy7Bk07A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Project Overview

### Problem Statement

**User side - "echo chamber"**

When music listeners use music streaming platforms, they might have experience of being in an **"echo chamber"**. The recommender algorithm might point back to the users' past listening experience and recommends songs that are very similar. This could give a feeling to users that they are "trapped" in a musical cohort. Some users might also be interested in music in the niche sectors or new sound for inspirations, but find it difficult to discover those contents as searching by keywords on song title, album name, artist name or even genre is often ineffective in this situation. They might not even have heard of any information about the artist or the song, let alone searching and discovering by keywords. A recommender algorithm that could pick up audio features and make recommendations for them would be very helpful then, and could potentially increase the user engagement on the streaming platforms.

**Artist side - "cold-start" problem for the long tail**

The market of artists (meaning musicians, used interchangeably) is a long-tail one in terms of popularity or the number of followers, which means there is actually a large amount of artists if you cut out the long tail. Inside the long tail, you could easily find that there are a lot of independent artists, niche artists and new comers. They might often encounter the cold-start problem, which means that their tracks might be at a disadvantaged position in the recommender system. A recommender algorithm that could **pick up audio features but not certain kinds of track record** and make recommendations could be more beneficial to the artists.

### Proposed Solution (Prototype)

#### "Adventure" Playlist - finding "relevant but novel" sound for users

This project is to explore and create a new playlist recommendation to discover music with variety for users and match the music of musicians in the long-tail market to potential fans using content-based recommendations with **"novelty-relevance" approach**. I intend to define a new metric of "novelty-relevance score" and explore this new way of recommendation.

**This approach aims to find relevant but novel sounding tracks for users, and it uses only audio features and tags so that artists in the long-tail market could also be benefitted.**

The playlist is called an "Adventure" playlist, and it contains a **customizable function for users to control the weighting of novelty** (against relevance) in the playlist when they want to adventure through the music in the database. The customization could be displayed as a slidebar in an actual app, and the users could control the playlist using the slidebar and see the playlist updating real-time.


## Project Organization

* `data`
    - Google drive: (google drive link: https://drive.google.com/drive/folders/1FFAypdO-jROIowRWARekAOx08oWfBxNZ?usp=sharing)
        - Music_Info.csv
        - User_Listening_History.csv
        - df_track_cleaned.csv
        - df_user_track.csv
        - df_track_vec.csv
        - df_kmeans.csv
        - df_track_label.csv
        - df_user_a.csv
        - algorithm.png

* `notebooks`
    - MusicRec_01_DataCleaning_EDA.ipynb
    - MusicRec_02_EDA.ipynb
    - MusicRec_03_Preprocessing.ipynb
    - MusicRec_04_Clustering.ipynb
    - MusicRec_05_Recommendations.ipynb
    - MusicRec_06_Appendix_Dataframes.ipynb

* `model`
    - kmeans.pkl

* `figures`

* `.gitignore`

* `environment.yml`
    - Conda environment specification

* `requirements.txt`
    - Dependencies for web app

* `README.md`



## Datasets

This is a rebuilt version and subset of The Million Song Dataset¹. It was built up with lastfm-spotify-tags-sim-userdata² (The Echo Nest Taste Profile Subset³ & lastfm-dataset-2020⁴), tagtraum genre annotations⁵, and Spotify API⁶.

It is extracted from https://www.kaggle.com/datasets/undefinenull/million-song-dataset-spotify-lastfm, where the two subsets of data "Music Info" and "User Listening History" are utilized here.

The "Music_Info" dataset contains three main types of data: high level meta-data of songs such as the artist, title and publishing year of a song, various audio features of songs, and tags and genres that are associated with the songs. The "User_Listening_History" dataset contains the playcounts on tracks that the users listened to.


## Credits & References

1. The Million Song Dataset: http://millionsongdataset.com/
2. lastfm-spotify-tags-sim-userdata: https://github.com/slettner/lastfm-spotify-tags-sim-userdata
3. The Echo Nest Taste Profile Subset: http://millionsongdataset.com/tasteprofile/
4. lastfm-dataset-2020: https://github.com/renesemela/lastfm-dataset-2020
5. tagtraum genre annotations: https://www.tagtraum.com/msd_genre_datasets.html
6. Spotify API: https://developer.spotify.com/documentation/web-api

Discussions about 'genre' and 'tags':
- https://speakerdeck.com/hendriks73/improving-genre-annotations-for-the-million-song-dataset
- https://www.tagtraum.com/download/schreiber_msdgenre_ismir2015.pdf

--------