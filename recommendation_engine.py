import pandas as pd
import numpy as np

def build_similarity_matrix(movie_data):
    # Build similarity matrix based on movie features
    
    # Create dummy variables for categorical features
    categorical_features = ["director", "genre"]
    movie_data_encoded = pd.get_dummies(movie_data, columns=categorical_features)
    
    # Calculate similarity matrix using cosine similarity
    features = movie_data_encoded.drop(["title"], axis=1)
    similarity_matrix = np.dot(features, features.T)
    
    return similarity_matrix

def recommend_movies(movie_data, similarity_matrix, user_id):
    # Generate movie recommendations for a given user
    
    # Get user's movie preferences
    user_movies = movie_data[movie_data["user_id"] == user_id]
    
    # Calculate user's average rating
    user_avg_rating = user_movies["rating"].mean()
    
    # Get similar movies based on user preferences
    similar_movies = similarity_matrix[user_movies.index]
    
    # Calculate weighted average rating of similar movies
    weighted_ratings = np.dot(similar_movies, movie_data["rating"]) / np.sum(similar_movies, axis=1)
    
    # Filter out movies already rated by the user
    unrated_movies = movie_data[movie_data["user_id"] != user_id]
    
    # Sort movies by weighted ratings
    sorted_movies = unrated_movies.sort_values(by=weighted_ratings, ascending=False)
    
    # Select top recommended movies
    recommended_movies = sorted_movies.head(5)["title"]
    
    return recommended_movies

def main():
    # Load preprocessed data
    movie_data = pd.read_csv("preprocessed_data.csv")
    
    # Build similarity matrix
    similarity_matrix = build_similarity_matrix(movie_data)
    
    # Generate movie recommendations for a user
    user_id = 1
    recommendations = recommend_movies(movie_data, similarity_matrix, user_id)
    print(f"Recommendations for User {user_id}:")
    print(recommendations)

if __name__ == '__main__':
    main()
