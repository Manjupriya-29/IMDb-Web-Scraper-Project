# imdb_scraper.py
# Script to scrape movie titles from IMDb's Top 250 list

import requests
from bs4 import BeautifulSoup
import csv

# Set headers to mimic a web browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# URL of the IMDb page to scrape
url = 'https://www.imdb.com/chart/top/'

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all movie title links
    movie_links = soup.find_all('a', href=lambda href: href and '/title/' in href)
    
    # Extract text and clean it
    movies = [link.text.strip() for link in movie_links if link.text.strip()]
    
    # Save to CSV file
    with open('imdb_top_movies.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Movie Title'])  # Write header
        for movie in movies:
            writer.writerow([movie])      # Write each movie
            
    print("Scraping successful! Data saved to 'imdb_top_movies.csv'.")
    
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")