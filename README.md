# Music Recommender System

A content-based Music Recommender System built using Machine Learning and deployed using Streamlit.  
The system recommends songs similar to a selected track using vectorization and cosine similarity.

---

## Overview

This project implements a **content-based recommendation system** that suggests songs based on similarity between tracks.

Instead of relying on user ratings or collaborative filtering, this system analyzes song features and computes similarity scores to generate recommendations.

The application is deployed as an interactive web app using **Streamlit**.

---

## Features

- Content-based recommendation approach  
- Cosine similarity for similarity measurement  
- Interactive web interface built with Streamlit  
- Precomputed similarity matrix for fast recommendations  
- Large model file handling using Git LFS  

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Git Large File Storage (LFS)  

---

## How It Works

### 1. Data Preprocessing
The dataset is cleaned and important textual features are combined to form a unified representation of each song.

### 2. Feature Extraction
Text features are transformed into numerical vectors using vectorization techniques.

### 3. Similarity Computation
Cosine similarity is calculated between song vectors to measure closeness.

### 4. Recommendation
When a user selects a song, the system retrieves the top similar songs based on similarity scores.

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

## Live Demo
You can access the deployed application here:
### Streamlit App:
https://musicrecommendersystem-t3sfhgne2unedyf9dmmnfd.streamlit.app/
