# from sqlDb import *
from readApi import *
import os
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    # pip install requirements.txt
    omdb_api_key = os.getenv("OMDb_API_KEY")
    omdb_url = os.getenv("OMDBb_URL")
    movie_name = "Dune"  # Example movie ID for The Dark Knight
    movie_data = get_movie_data(movie_name, omdb_api_key, omdb_url)
    if movie_data:
        print(f"Title: {movie_data['Title']}")
        print(f"Release Year: {movie_data['Year']}")
        # Access other data points from the dictionary
    else:
        print("Failed to retrieve movie data.")
