import pandas as pd

def preprocess_data():
    # Read movie dataset from a CSV file
    movie_data = pd.read_csv("movies.csv")
    
    # Perform data preprocessing steps
    
    # Drop duplicate rows
    movie_data.drop_duplicates(inplace=True)
    
    # Fill missing values
    movie_data.fillna(value={"director": "Unknown", "genre": "Unknown"}, inplace=True)
    
    # Feature engineering
    movie_data["year"] = movie_data["release_date"].str[-4:]
    
    # Remove unnecessary columns
    movie_data = movie_data.drop(["release_date", "runtime"], axis=1)
    
    # Normalize numerical columns
    movie_data["rating"] = movie_data["rating"] / 10
    
    # Return preprocessed data
    return movie_data

def main():
    preprocessed_data = preprocess_data()
    preprocessed_data.to_csv("preprocessed_data.csv", index=False)
    print("Data preprocessing completed.")

if __name__ == '__main__':
    main()
