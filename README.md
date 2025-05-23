# RYM to Letterboxd Migration Tool

Convert your exported [Rate Your Music](rateyourmusic.com) film catalog into a format ready for import into [Letterboxd](themoviedb.org).

## Getting Started

This script uses TMDB's API to find most likely match to the each film in your RYM catalog based on the information provided. You'll need an API key to run the script successfully.

1. Go to themoviedb.org/account/signup and create a free account.
2. After logging in, go to your API settings.
3. Click "Create".
4. Fill out the form (you can just say it's for personal use).
5. Copy your API key and paste it in `.env`.

## Exporting from RYM

1. Go to your profile in RYM and click 'Export your film catalog'.
2. Save the catalog as a `.txt` file (called `export_film_catalog.txt`) to this project folder.

## Creating Import File

1. Clone this repo.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python rym2letterboxd.py
    ```

## Output
A file called `import_film_catalog.csv` ready to import into Letterboxd.

## Importing into Letterboxd
1. Go to `letterboxd.com/import` and click 'SELECT A FILE'.
2. Select the newly created `import_film_catalog.csv`.
3. Review the Import summary, then click 'IMPORT FILMS'.
