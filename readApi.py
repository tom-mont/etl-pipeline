import requests


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
            print(data['Title'])
            return data
        else:
            print(f"Error retrieving data: {data['Error']}")
    else:
        print(f"API request failed with status code: {response.status_code}")

    return None
