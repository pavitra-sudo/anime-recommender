from fastapi import FastAPI 

aniapp = FastAPI()

@aniapp.get("/")
def read_root():
    return { "Welcome to the Anime Recommendation Sytem!"}

@aniapp.get("/recommend")
def get_recommendation(title: str = "Death Note"):
    return {
        "input_title": title,
        "recommendations": ["Code Geass", "Psycho-Pass", "Monster"]
    }
    
