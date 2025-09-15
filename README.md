# IMDb Top Movies Web Scraper

A Python-based web scraping project that extracts the first batch of movie titles from IMDb's "Top 250" chart. This project demonstrates foundational skills in data collection, HTTP requests, HTML parsing, and data export—essential for any aspiring Data Analyst.

**Website Source:** [IMDb Top 250 Movies](https://www.imdb.com/chart/top/)

## 📁 Project Files

*   `imdb_scraper.py` - The main Python script.
*   `imdb_top_movies.csv` - The output dataset file.
*   `README.md` - This file.

## 🎯 Project Overview

This script automates the process of collecting the initially loaded movie data from the IMDb website. It successfully handles common scraping challenges like access denial and parses HTML to transform unstructured web data into a structured, analysis-ready CSV file.

## 🛠️ Tools & Skills Used

**Programming Language**:

<img src="https://img.icons8.com/color/48/000000/python.png" width="16" height="16"/> Python - The core programming language used for scripting the scraper.

**Libraries & Frameworks**:

Requests - For making HTTP requests to fetch the website's HTML content.

BeautifulSoup4 - For parsing HTML and extracting specific data elements.

CSV (Python Standard Library) - For saving the extracted data to a structured file.

**Core Data Analyst Skills Demonstrated**:

Web Scraping - Automating data collection from a live website.

HTTP Protocol Understanding - Handling headers (User-Agent) and status codes (200, 403).

HTML Parsing - Navigating and querying Document Object Model (DOM) structure to find data.

Data Cleaning - Preprocessing raw text (e.g., removing whitespace) to create clean data.

Data Wrangling - Transforming unstructured web data into a structured tabular format (CSV).

Problem-Solving - Diagnosing and resolving issues like access denial and missing modules.

**Development Tools**:

Visual Studio Code (VS Code) - Code editor for writing and debugging the script.

Command Prompt / Terminal - For executing the script and managing Python environments.

Git & GitHub - For version control and project portfolio hosting.

## 🔧 Technical Process

The project followed a clear data collection pipeline:

1.  **Data Fetching:** Used the `requests` library to retrieve the HTML source code of the IMDb page.
2.  **Access Management:** Overcame a `403 Forbidden` error by adding a `User-Agent` header to mimic a web browser.
3.  **HTML Parsing:** Employed `BeautifulSoup` to navigate and parse the complex HTML structure.
4.  **Data Extraction:** Identified and targeted specific HTML elements (`<a>` tags with `href` containing `/title/`) to isolate movie titles from the page's initial load.
5.  **Data Cleaning:** Cleaned the extracted text by removing whitespace with `.strip()`.
6.  **Data Export:** Saved the refined list of titles into a CSV file using Python's `csv` module.

## 📊 Output Data

The final output is a clean CSV file named `imdb_top_movies.csv`. The file contains a single column with the first set of movie titles loaded on the page.

*   **Movie Title:** The names of the top-listed movies.

[View the CSV File](./imdb_top_movies.csv)

## ⚠️ Important Note on Data Volume

A key learning from this project was encountering **dynamic content loading**. The IMDb page uses JavaScript to load more movies as the user scrolls. Since this script uses `requests` (which only fetches the initial, static HTML), it captured the first set of movies that are loaded when the page first opens. that is first 25 movies in the list'.

This is not a limitation of the code but a fundamental characteristic of modern websites. It provides a clear learning path for advanced tools like **Selenium** to handle dynamic content in the future.

## 🚀 How to Run

1.  **Ensure Python is installed** on your system.
2.  **Install the required libraries** using pip:
    ```bash
    pip install requests beautifulsoup4
    ```
3.  **Run the scraping script** from your terminal or command prompt:
    ```bash
    python imdb_scraper.py
    ```
4.  Upon successful execution, the script will create the `imdb_top_movies.csv` file in the same directory.

## 📝 Code Snippet

```python
import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.imdb.com/chart/top/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
movie_links = soup.find_all('a', href=lambda href: href and '/title/' in href)

movies = [link.text.strip() for link in movie_links if link.text.strip()]

with open('imdb_top_movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie Title'])
    for movie in movies:
        writer.writerow([movie])

print("Data successfully saved to imdb_top_movies.csv!")

```



## Conclusion


This project successfully demonstrates the core workflow of web scraping: from fetching raw HTML and overcoming access barriers to parsing, extracting, and finally storing data in a structured format. While the technical goal was to collect movie titles from IMDb, the greater achievement was navigating and solving real-world challenges like HTTP errors and dynamic content limitations.

Completing this end-to-end pipeline provides a strong foundation in data acquisition—a critical skill for any data analyst. The experience also clearly outlines the path for future growth, specifically learning to use tools like Selenium to handle more complex, JavaScript-driven websites. This project is a solid first step into the practical world of data collection.
