import pandas as pd
import mysql.connector
import re

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="movie_db2"
)

# Function to fetch movie data from the database into a DataFrame
def fetch_movies_from_database():
    query = "SELECT title, movie_id, title AS original_title FROM movie"
    cursor = db_connection.cursor()
    cursor.execute(query)
    movies_data = cursor.fetchall()
    columns = ['title', 'movieId', 'original_title']  # Define column names
    movies_df = pd.DataFrame(movies_data, columns=columns)
    return movies_df

# Normalize movie titles by moving leading articles to the end
def normalize_title(title):
    if title.lower().startswith(("a ", "an ", "the ")):
        leading_article = re.match(r'^(a|an|the|les) ', title.lower()).group(0)
        processed_title = title[len(leading_article):] + ", " + leading_article.capitalize().strip()
        return processed_title
    return title

# Read CSV files into DataFrames
movies_csv_filename = 'ml-latest-small/ml-latest-small/movies1.csv'  # Adjust filenames as needed
users_csv_filename = 'ml-latest-small/ml-latest-small/ratings1.csv'
movies_data = pd.read_csv(movies_csv_filename)
users_data = pd.read_csv(users_csv_filename)

# Fetch movie data from the database
database_movies = fetch_movies_from_database()

# Normalize movie titles in the database DataFrame
database_movies['title'] = database_movies['title'].apply(normalize_title)

# Keep track of matched and unmatched movies
matched_movies = []
unmatched_movies = []

# Iterate through each movie in the CSV file
for index, row in movies_data.iterrows():
    # Normalize movie title for comparison
    csv_movie_title = normalize_title(row['title']).strip()
    # Check if normalized movie title exists in the database
    if csv_movie_title in database_movies['title'].values:
        # If a match is found, update the ID in both movies and users CSV files
        movie_id = database_movies.loc[database_movies['title'] == csv_movie_title, 'movieId'].values[0]
        movies_data.at[index, 'movieId'] = movie_id
        # Update movie ID in the users CSV file
        users_data.loc[users_data['movieId'] == row['movieId'], 'movieId'] = movie_id
        matched_movies.append(row['title'])
    else:
        # Keep track of unmatched movies
        unmatched_movies.append(row['title'])

# Remove rows from the users CSV file corresponding to the unmatched movies
users_data = users_data[~users_data['movieId'].isin(movies_data[movies_data['title'].isin(unmatched_movies)]['movieId'])]

# Print unmatched movies
print("Unmatched movies:")
for movie in unmatched_movies:
    print(movie)
print(len(unmatched_movies))

# Filter movies from dataset not present in the database
movies_data = movies_data[movies_data['title'].isin(matched_movies)]

# Update titles back to original titles in the movies CSV file
for index, row in movies_data.iterrows():
    original_title = database_movies.loc[database_movies['movieId'] == row['movieId'], 'original_title'].values[0]
    movies_data.at[index, 'title'] = original_title

# Save updated DataFrames back to CSV files
movies_data.to_csv(movies_csv_filename, index=False)
users_data.to_csv(users_csv_filename, index=False)
