import pandas as pd

# Load dataset once here (so you don't load it every time)
df = pd.read_csv("anime.csv")

def get_simple_recommendations(anime_name, n=5):
    if anime_name not in df['name'].values:
        return ["Anime not found. Try another title."]
    
    anime_genres = df[df['name'] == anime_name]['genre'].values[0]
    if pd.isna(anime_genres):
        return ["No genre info available for this anime."]
    
    recommended = []
    for _, row in df.iterrows():
        if row['name'] != anime_name and pd.notna(row['genre']):
            if any(genre in row['genre'] for genre in anime_genres.split(',')):
                recommended.append(row['name'])
            if len(recommended) >= n:
                break
    return recommended if recommended else ["No similar anime found."]
