# Music Recommender System

This project is a Music Recommender System built with Python, Streamlit, and various machine learning techniques. It provides personalized music recommendations based on user preferences.

## Features

- Personalized Recommendations: Suggests songs based on user input or specific genre and artist choices.
- Streamlit Interface: A user-friendly web interface for interaction.
- Efficient Computation: Utilizes precomputed similarity scores to enhance recommendation speed.

## Libraries Used

- streamlit: For creating the web interface
- pandas: For data handling and manipulation
- numpy: For numerical computations
- scikit-learn: For machine learning utilities
- fasttext from gensim.models: For fast, efficient text processing in model similarity calculations
- pickle: To load the precomputed model

## Setup and Installation

1. Clone the repository:
- git clone https://github.com/Amartya133/Music_Recommender_System.git
- cd Music_Recommender_System
2. Install the required packages: pip install -r requirements.txt
3. Run the application: streamlit run app.py

## Dataset

The model was trained on a dataset of Spotify songs with different genres and their audio features: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset/code?datasetId=2570056&sortBy=voteCount

## Usage

To get started with the Music Recommender System app, follow these steps to receive song recommendations based on your preferences:
1. Run the Application: Follow the setup and execution instructions above to launch the app on your local environment or public URL.
2. Input Song Information: Enter a song title or choose one from the pre-populated list within the app's interface.
3. View Recommendations: Based on your input, the app will display a curated list of recommended songs using the similarity model.
