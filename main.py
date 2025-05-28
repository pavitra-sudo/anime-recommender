from fastapi import FastAPI 

aniapp = FastAPI()

@aniapp.get("/")
def read_root():
    return { "Welcome to the Anime Recommendation Sytem!"}

@aniapp.get("/recommend")
def recommend(title: str = "Death Note"):
    try:
        df = pd.read_csv("anime.csv")
        results = get_recommendations(title, df)
        return {"input_title": title, "recommendations": results}
    except Exception as e:
        return {"error": str(e)}

    
    
import pandas as pd

# Load the dataset
df = pd.read_csv("anime.csv")


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def get_recommendations(anime_name, df, n=5):
    df = df.dropna(subset=['genre'])  # Remove rows with missing genres
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genre'])

    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df.index, index=df['name']).drop_duplicates()

    if anime_name not in indices:
        return ["Anime not found. Try another title."]

    idx = indices[anime_name]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    anime_indices = [i[0] for i in sim_scores]
    
    return df['name'].iloc[anime_indices].tolist()
