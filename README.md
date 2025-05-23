# RYM to Letterboxd Importer

Convert your exported RateYourMusic film catalog into a format ready for import into [Letterboxd](https://letterboxd.com).

## Features
- Corrects missing articles like "The", "La", etc.
- Matches movies using TMDb API with popularity ranking
- Exports a clean CSV file for Letterboxd import

## Exporting from RYM

1. Go to your profile in RYM and click 'Export your film catalog'.
2. Save the catalog as a `.txt` file (called `export_film_catalog.txt`) to this project folder.

## Creating Import File

1. Clone this repo.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Copy `.env.example` to `.env` and set your TMDb API key:

    ```bash
    cp .env.example .env
    ```

4. Run the script:

    ```bash
    python rym2letterboxd.py
    ```

## Output
A file called `import_film_catalog.csv` ready to import into Letterboxd.

## Importing into Letterboxd
1. Go to `https://letterboxd.com/import` and click 'SELECT A FILE'.
2. Select the newly created `import_film_catalog.csv`.
3. Review the Import summary, then click 'IMPORT FILMS'.
