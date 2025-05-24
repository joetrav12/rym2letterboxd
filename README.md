# RYM to Letterboxd Migration Tool

Convert your exported [Rate Your Music](https://rateyourmusic.com) film catalog into a format ready for import into [Letterboxd](https://letterboxd.com).

## Requirements

You'll need [Python v3.7+](https://python.org/downloads) and [Pip v19.0+](https://pip.pypa.io/en/stable/installation) installed to run this script.

To confirm you have them installed, run:

```bash
python --version
pip --version
```

## Setup

1. Clone this repo:

    ```bash
    git clone https://github.com/joetrav12/rym2letterboxd
    ```

## TMDB API Key

This script uses TMDB's API to find the most likely match to each film in your RYM catalog. You'll need an API key to run this script.

1. Go to https://themoviedb.org/account/signup and create a free account.
2. After logging in, go to [API Settings](https://themoviedb.org/settings/api).
3. Click "Create".
4. Fill out the form (you can just say it's for personal use).
5. Copy your API key (you'll use it in a later step).

## Exporting from RYM

1. Go to your profile in RYM and click 'Export your film catalog'.
2. Save the catalog as a `.txt` file (called `export_film_catalog.txt`) to this project folder.

## Creating Import File

1. Navigate to this project directory:

    ```bash
    cd rym2letterboxd
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file:

    ```bash
    touch .env
    ```

4. Add your key in `.env`:

    ```ini
    TMDB_API_KEY='your_api_key_here'
    ```

3. Run the script:

    ```bash
    python rym2letterboxd.py
    ```
    or
    ```bash
    python3 rym2letterboxd.py
    ```

## Output
The script will generate `import_film_catalog.csv` in the project directory. This file is formatted according to [Letterboxd's import guidelines](https://letterboxd.com/help/importing-data).

## Importing into Letterboxd
1. Go to https://letterboxd.com/import and click 'SELECT A FILE'.
2. Select the newly created `import_film_catalog.csv`.
3. Review the Import summary, then click 'IMPORT FILMS'.
