# Music Recommender System

A content-based Music Recommender System built using Machine Learning and deployed using Streamlit. The system recommends similar songs using cosine similarity and dynamically fetches album cover images using the **iTunes Search API**.

---

## Live Application

You can access the deployed application here:

### Streamlit App

https://musicrecommendersystem-t3sfhgne2unedyf9dmmnfd.streamlit.app/

---

## Overview

This project implements a content-based recommendation system that suggests songs based on similarity between tracks.

Instead of relying on user ratings or collaborative filtering, the system analyzes song features and computes similarity scores to generate recommendations.

The application is deployed as an interactive web app using Streamlit.

---

## Features

- Content-based recommendation approach
- Cosine similarity for similarity measurement
- iTunes Search API integration for album artwork
- Dynamic album cover retrieval using song titles and artist names (when available)
- Interactive Streamlit interface
- Top 5 similar song recommendations
- Default fallback image when album artwork is unavailable
- Large model file handling using Git LFS

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Requests
- Streamlit
- iTunes Search API
- Git Large File Storage (LFS)

---

## How It Works

### 1. Data Preprocessing

Implemented in the Jupyter Notebook file `Music_recommender_system.ipynb`.

The notebook performs:

- Dataset cleaning
- Feature engineering
- Vectorization
- Cosine similarity computation
- Model serialization using pickle

This generates:

- `music.pkl`
- `similarity.pkl`

### 2. Recommendation Logic

The application loads the precomputed pickle files, identifies the selected track, sorts similarity scores, and returns the top five most similar songs.

### 3. Album Artwork Retrieval

The system uses Apple's **iTunes Search API** to dynamically retrieve album cover images.

- Searches using the song title and artist name when available.
- Retrieves album artwork URLs from the API response.
- Uses Streamlit caching to reduce repeated API requests.
- Displays a default fallback image if artwork cannot be retrieved.

### 4. Streamlit Interface

- `st.selectbox()` for song selection
- `st.button()` to trigger recommendations
- `st.columns(5)` to display top 5 results
- `st.image()` to show album covers

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/Amartya133/Music_Recommender_System.git
cd Music_Recommender_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## API Integration

This project uses the public iTunes Search API for retrieving album artwork.

API endpoint:

https://itunes.apple.com/search

The API does not require Spotify credentials or a separate API key.

---

## Security Note

No Spotify Client ID or Client Secret is required in the current implementation. API requests for album artwork are made through the iTunes Search API.

---

## Author

Amartya Nayak
