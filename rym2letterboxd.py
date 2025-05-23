import sys
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise RuntimeError("TMDB_API_KEY not set in .env file")

TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

def normalize(title):
    """
    Normalize a movie title for easier matching:
    - Lowercase
    - Remove leading articles like 'The', 'La', 'Le', etc.
    """
    title = title.lower().strip()
    if title.startswith(('the ', 'la ', 'le ', 'el ', 'les ', 'los ')):
        title = title.split(' ', 1)[1]
    return title

def search_tmdb_movie(title, year):
    """
    Query TMDB for a movie by title and year.
    Return the first result if found, else None.
    """
    params = {
        'api_key': API_KEY,
        'query': title,
        'year': year
    }
    response = requests.get(TMDB_SEARCH_URL, params=params)
    if response.status_code != 200:
        print(f"Error {response.status_code} for title: {title}")
        return None

    data = response.json()
    return data['results'][0] if data['results'] else None

def find_best_match(title, year):
    """
    Given a title and year, search TMDB for the best match.
    Tries both the raw title and 'The' + title.
    Picks based on normalized match and popularity.
    """
    tmdb_search = search_tmdb_movie(title, year)
    tmdb_search_the = search_tmdb_movie('The ' + title, year)

    all_results = []
    if tmdb_search:
        all_results.append(tmdb_search)
    if tmdb_search_the:
        all_results.append(tmdb_search_the)

    if not all_results:
        return title  # fallback: original title

    input_norm = normalize(title)

    # Try to find a good match ignoring leading articles
    possible_matches = []
    for movie in all_results:
        movie_title_norm = normalize(movie['title'])
        if movie_title_norm == input_norm:
            possible_matches.append(movie)

    if possible_matches:
        # Pick most popular among good matches
        best_match = max(possible_matches, key=lambda x: x['popularity'])
    else:
        # If no good matches, pick most popular overall
        best_match = max(all_results, key=lambda x: x['popularity'])

    return best_match['title']

def main(argv):
    print('Processing...')
    # Load exported RYM film catalog
    try:
        rym_films = pd.read_csv('export_film_catalog.txt')
    except FileNotFoundError:
        print("Error: 'export_film_catalog.txt' not found.")
        sys.exit(1)

    years = []
    watched_dates_formatted = []

    for index, (_, row) in enumerate(rym_films.iterrows()):
        title = row['Title']

        # Fix encoding issues like '&amp;'
        if '&amp;' in title:
            title_split = title.split('&amp;')
            title = title_split[0] + 'and' + title_split[1]
            rym_films.loc[index, 'Title'] = title

        # Extract release year
        year = row['Release_Date'].split('/')[0]
        years.append(year)

        # Format watched date
        watched_date_split = row['Catalog_Date'].split('/')
        watched_date_formatted = '-'.join(watched_date_split)
        watched_dates_formatted.append(watched_date_formatted)

        # Find best matching title from TMDB
        corrected_title = find_best_match(title, year)
        rym_films.loc[index, 'Title'] = corrected_title

    # Update DataFrame with new columns
    rym_films['Year'] = years
    rym_films['WatchedDate'] = watched_dates_formatted

    # Rename and drop unnecessary columns
    rym_films.rename(columns={'Rating': 'Rating10'}, inplace=True)
    rym_films.drop(columns=['Film_ID', 'Release_Date', 'Ownership', 'Catalog_Date'], inplace=True)

    # Export cleaned-up file
    rym_films.to_csv('import_film_catalog.csv', index=False)

    print('Done.')

if __name__ == "__main__":
    main(sys.argv)
