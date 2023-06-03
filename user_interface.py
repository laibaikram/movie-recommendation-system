from recommendation_engine import recommend_movies

def get_user_preferences():
    # Get user preferences for movie recommendations
    
    # Get user input for movie genre preference
    genre_preference = input("Enter your preferred movie genre: ")
    
    # Get user input for movie director preference
    director_preference = input("Enter your preferred movie director: ")
    
    # Create user preferences dictionary
    user_preferences = {"genre": genre_preference, "director": director_preference}
    
    return user_preferences

def display_recommendations(recommendations):
    # Display movie recommendations to the user
    print("Recommended Movies:")
    for movie in recommendations:
        print(movie)

def main():
    # Get user preferences for movie recommendations
    user_preferences = get_user_preferences()
    
    # Generate movie recommendations based on user preferences
    recommendations = recommend_movies(user_preferences)
    
    # Display movie recommendations
    display_recommendations(recommendations)

if __name__ == '__main__':
    main()
