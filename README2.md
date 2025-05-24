# RYM to Letterboxd Migration Tool

Convert your exported [Rate Your Music](https://rateyourmusic.com) film catalog into a format ready for import into [Letterboxd](https://letterboxd.com).

## Requirements

You'll need [Python v3.7+](https://www.python.org/downloads) and [Pip v19.0+](https://pip.pypa.io/en/stable/installation) installed to run this script.

To confirm you have them installed, run:

```bash
python --version
pip --version
```

## Setup

1. Clone this repo:

    ```bash
    git clone https://github.com/joetrav12/rym2letterboxd
    cd rym2letterboxd
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file or rename the provided example:

    ```bash
    cp .env.example .env
    ```

4. Open `.env` and paste your TMDB API key:

    ```ini
    TMDB_API_KEY=your_api_key_here
    ```

## TMDB API Key

This script uses TMDB's API to find the most likely match for each film in your RYM catalog.

1. Go to https://themoviedb.org/account/signup and create a free account.
2. After logging in, go to [API Settings](https://www.themoviedb.org/settings/api).
3. Click "Create".
4. Fill out the form (you can select "personal use").
5. Copy your API key and use it in your `.env` file as shown above.

## Exporting from RYM

1. Go to your profile on RateYourMusic and click **Export your film catalog**.
2. Save the export file as `export_film_catalog.txt` in the root of this project directory.

## Running the Script

With your `.env` configured and RYM export in place, run:

```bash
python rym2letterboxd.py
```

or, if using `python3`:

```bash
python3 rym2letterboxd.py
```

## Output

A file named `import_film_catalog.csv` will be created
