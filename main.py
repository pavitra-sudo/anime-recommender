from fastapi import FastAPI
from recommendations import get_cosine_recommendations

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smarter Anime Recommendation System (Cosine Similarity)"}

@app.get("/recommend")
def recommend(title: str):
    results = get_cosine_recommendations(title)
    return {"title": title, "recommendations": results}
