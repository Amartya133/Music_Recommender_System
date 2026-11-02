
import pickle
import streamlit as st
import requests

# iTunes API album cover retrieval
@st.cache_data(ttl=86400)
def get_song_album_cover_url(song_name, artist_name):

    try:
        url = "https://itunes.apple.com/search"

        params = {
            "term": f"{song_name} {artist_name}",
            "entity": "song",
            "limit": 5
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data["resultCount"] > 0:
            image_url = data["results"][0].get("artworkUrl100")

            if image_url:
                return image_url.replace("100x100", "600x600")

    except Exception as e:
        print("Album cover error:", e)

    return "https://i.postimg.cc/0QNxYz4V/social.png"


# Recommendation function
def recommend(song):

    index = music[music['track_name'] == song].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_music_names = []
    recommended_music_posters = []

    for i in distances[1:6]:

        song_name = music.iloc[i[0]]['track_name']
        artist_name = music.iloc[i[0]]['artists']

        print(song_name)
        print(artist_name)

        poster = get_song_album_cover_url(
            song_name,
            artist_name
        )

        recommended_music_names.append(song_name)
        recommended_music_posters.append(poster)

    return recommended_music_names, recommended_music_posters


# Streamlit application
st.header('Music Recommender System')

music = pickle.load(open('music.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music['track_name'].values

selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):

    recommended_music_names, recommended_music_posters = recommend(
        selected_music
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    columns = [col1, col2, col3, col4, col5]

    for i, col in enumerate(columns):

        with col:
            st.text(recommended_music_names[i])
            st.image(recommended_music_posters[i])
