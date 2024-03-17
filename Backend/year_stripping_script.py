import pandas as pd
import re

def normalize_title(title):
    # Remove release years in brackets
    title = re.sub(r'\s*\(\d{4}\)$', '', title)
    # Remove any text within brackets
    title = re.sub(r'\s*\([^)]*\)', '', title)
    title = title.strip()
    return title


if __name__ == "__main__":
    # Read CSV file into a DataFrame
    movies_csv_filename = 'movies.csv'  # Adjust filename as needed
    movies_data = pd.read_csv(movies_csv_filename)

    # Apply title normalization
    movies_data['title'] = movies_data['title'].apply(normalize_title)

    # Save normalized data back to CSV file
    movies_csv_filename = 'movies1.csv'
    movies_data.to_csv(movies_csv_filename, index=False)
    print("Movie titles normalized and saved successfully.")

