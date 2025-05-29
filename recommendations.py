import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("anime.csv")

# Fill missing genres with empty string
df['genre'] = df['genre'].fillna('')

# Vectorize genres using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map anime titles to index
anime_indices = pd.Series(df.index, index=df['name']).drop_duplicates()

def get_cosine_recommendations(title, n=5):
    if title not in anime_indices:
        return ["Anime not found."]
    
    idx = anime_indices[title]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by highest similarity (excluding itself)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    
    # Get recommended anime indices
    anime_indices_list = [i[0] for i in sim_scores]
    
    return df['name'].iloc[anime_indices_list].tolist()
