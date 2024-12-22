import pandas as pd

import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID = "8b96a50a9c2f49af91370ae136d96661"
CLIENT_SECRET = "e87957a94748463ab05a908cd3d3f32e"


client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def  fetch_poster(music_title):
    search_query = f"track:{music_title} "
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    return "https://i.postimg.cc/0QNxYz4V/social.png"


music_dict = pickle.load(open('C:\\workspace\\sem-5Project\\archive\\musicnew.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open("C:\\workspace\\sem-5Project\\archive\\similaritiesnew.pkl", 'rb'))

 
def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_music = []
    recommended_music_poster = []

    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music_title)

        poster_url = fetch_poster(music_title)
       
        recommended_music_poster.append(
            poster_url if poster_url else 'https://via.placeholder.com/150')  
            

    return recommended_music, recommended_music_poster


# Load data

st.title('Music Recommendation System')

selected_music_name = st.selectbox('Select a music you like', music['title'].values)

if st.button('Recommend'):
    if selected_music_name:  
        try:
            names, posters = recommend(selected_music_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])
            with col2:
                st.text(names[1])
                st.image(posters[1])
            with col3:
                st.text(names[2])
                st.image(posters[2])
            with col4:
                st.text(names[3])
                st.image(posters[3])
            with col5:
                st.text(names[4])
                st.image(posters[4])
        except IndexError:
            st.error("No recommendations found. Please try another song.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please select a music title.")