import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_movie_data(movie_name, api_key, url):
    """
    Retrieves movie data from OMDb API for a given movie ID.

    Args:
        api_key (str): Your OMDb API key.
        movie_id (str): The ID of the movie to retrieve data for.

    Returns:
        dict: A dictionary containing the movie data if successful,
            None otherwise.
    """

    # Build the API request URL
    url = f"{url}?apikey={api_key}&t={movie_name}"

    # Send GET request to the API
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Check for valid response (error key might be present)
        if "Error" not in data:
            print(data)
            return data
        else:
            print(f"Error retrieving data: {data['Error']}")
    else:
        print(f"API request failed with status code: {response.status_code}")

    return None


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error:`{err}`")


create_movie_table = """
    CREATE TABLE movie (
        title VARCHAR(20) PRIMARY KEY,
        year INT NOT NULL
    );
"""

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
