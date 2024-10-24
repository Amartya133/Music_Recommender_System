import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import gdown

CLIENT_ID = "5fbf8f665a2448c18da93e67c994da46"
CLIENT_SECRET = "c2dcf0cf5b084045b839ebba8b075976"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(track_id):
    track = sp.track(track_id)

    if track and "album" in track and "images" in track["album"]:
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        # Default image URL if track not found
        return "https://i.postimg.cc/0QNxYz4V/social.png"


def recommend(song):
    index = music[music['track_name'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        track_id = music.iloc[i[0]].track_id
        print(track_id)
        print(music.iloc[i[0]].track_name)
        recommended_music_posters.append(get_song_album_cover_url(track_id))
        recommended_music_names.append(music.iloc[i[0]].track_name)

    return recommended_music_names,recommended_music_posters

st.header('Music Recommender System')
music = pickle.load(open('music.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['track_name'].values
selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names,recommended_music_posters = recommend(selected_music)
    col1, col2, col3, col4, col5= st.columns(5)
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

file_id = "1VBuqoG5b9XEeY2QHxpdC6SkdlXUdrRvW"
url = f"https://drive.google.com/uc?id={file_id}"
output = 'similarity.pkl'

# Download the file
gdown.download(url, output, quiet=False)



