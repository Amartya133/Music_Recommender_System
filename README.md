# Music Recommender System

A content-based Music Recommender System built using Machine Learning and deployed using Streamlit. The system recommends similar songs and dynamically fetches album cover images using the Spotify API.

---

## Live Application

You can access the deployed application here: 

### Streamlit App: 

https://musicrecommendersystem-t3sfhgne2unedyf9dmmnfd.streamlit.app/

---

## Overview

This project implements a content-based recommendation system that suggests songs based on similarity between tracks.

Instead of relying on user ratings or collaborative filtering, this system analyzes song features and computes similarity scores to generate recommendations.

The application is deployed as an interactive web app using Streamlit.

---

## Features

- Content-based recommendation approach
- Cosine similarity for similarity measurement
- Spotify API integration for album artwork
- Interactive Streamlit interface
- Top 5 similar song recommendations
- Large model file handling using Git LFS

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Spotipy
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

### 3. Spotify API Integration

The system uses Spotipy to authenticate with Spotify using client credentials and fetch album cover images dynamically using `track_id`.

If a track is unavailable, a default fallback image is used.

### 4. Streamlit Interface

- `st.selectbox()` for song selection
- `st.button()` to trigger recommendations
- `st.columns(5)` to display top 5 results
- `st.image()` to show album covers

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

## Security Note

Spotify API credentials should be stored using environment variables or Streamlit secrets in production deployments.

---

## Author

Amartya Nayak
