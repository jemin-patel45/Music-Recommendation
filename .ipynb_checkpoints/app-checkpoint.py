
# import pickle
# import streamlit as st
# import spotipy


# from spotipy.oauth2 import SpotifyClientCredentials

# CLIENT_ID = "8b96a50a9c2f49af91370ae136d96661"
# CLIENT_SECRET = "e87957a94748463ab05a908cd3d3f32e"

# # Initialize the Spotify client
# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# def get_song_album_cover_url(song_name, artist_name):
#     search_query = f"track:{song_name} artist:{artist_name}"
#     results = sp.search(q=search_query, type="track")

#     if results and results["tracks"]["items"]:
#         track = results["tracks"]["items"][0]
#         album_cover_url = track["album"]["images"][0]["url"]
#         print(album_cover_url)
#         return album_cover_url
#     else:
#         return "https://i.postimg.cc/0QNxYz4V/social.png"

# def recommend(song):
#     index = music[music['song'] == song].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_music_names = []
#     recommended_music_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         artist = music.iloc[i[0]].artist
#         print(artist)
#         print(music.iloc[i[0]].song)
#         recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
#         recommended_music_names.append(music.iloc[i[0]].song)

#     return recommended_music_names,recommended_music_posters

# st.header('Music Recommender System')
# music = pickle.load(open('C:\\workspace\\sem-5Project\\archive\\music.pkl','rb'))
# similarity = pickle.load(open('C:\\workspace\\sem-5Project\\archive\\similarities.pkl','rb'))

# music_list = music['title'].values
# selected_movie = st.selectbox(
#     "Type or select a song from the dropdown",
#     music_list
# )

# if st.button('Show Recommendation'):
#     recommended_music_names,recommended_music_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5= st.columns(5)
#     with col1:
#         st.text(recommended_music_names[0])
#         st.image(recommended_music_posters[0])
#     with col2:
#         st.text(recommended_music_names[1])
#         st.image(recommended_music_posters[1])

#     with col3:
#         st.text(recommended_music_names[2])
#         st.image(recommended_music_posters[2])
#     with col4:
#         st.text(recommended_music_names[3])
#         st.image(recommended_music_posters[3])
#     with col5:
#         st.text(recommended_music_names[4])
#         st.image(recommended_music_posters[4])




import pickle
import streamlit as st
import spotipy


from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "8b96a50a9c2f49af91370ae136d96661"
CLIENT_SECRET = "e87957a94748463ab05a908cd3d3f32e"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


# Replace with a valid fallback image URL




def recommend(song):
    index = music[music['title'] == song].index[0]
    distances = similarity[index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music_names = []
    recommended_music_posters = []
    for i in music_list:
        # fetch the movie poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        # recommended_music_names.append(music.iloc[i[0]].song)
        recommended_music_names.append(artist)
        poster_url = get_song_album_cover_url(music.iloc[i[0]].song, artist)
        # recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_posters.append(poster_url if poster_url else 'https://via.placeholder.com/150')
    return recommended_music_names,recommended_music_posters


st.header('Music Recommender System')

# Load the data
music = pickle.load(open('C:\\workspace\\sem-5Project\\archive\\music.pkl', 'rb'))
similarity = pickle.load(open('C:\\workspace\\sem-5Project\\archive\\similarities.pkl', 'rb'))

# Verify column names
st.write(music.columns)  # Check the column names

# If the column is not 'song', use the correct column
music_list = music['song'].values if 'song' in music.columns else music['title'].values

# Streamlit UI
selected_song = st.selectbox("Type or select a song from the dropdown", music_list)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: 
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])

