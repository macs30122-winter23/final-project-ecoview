'''
This file is responsible for scraping the Policy_Efficiency_Score calculated by ACEEE from all U.S. states between the years 2018 and 2021.
'''

# Import necessary libraries
import requests  # for making HTTP requests
from bs4 import BeautifulSoup  # for parsing HTML content

# Define the URL to scrape
url = 'https://database.aceee.org/state/2021-scorecard-data-table'

# Make an HTTP GET request to the URL and store the response object
response = requests.get(url)

# Parse the HTML content of the response object using Beautiful Soup and store it in a soup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table that contains the state scores, based on the class name of the table
# Note that this assumes the class name of the table will not change over time
table = soup.find('table', {'class': 'views-table cols-7'})

# Get the rows of the table, which are enclosed in <tr> tags
rows = table.find_all('tr')

# Loop through the rows of the table, skipping the first row (which contains column headers)
for row in rows[1:]:

    # Get the columns of the row, which are enclosed in <td> tags
    cols = row.find_all('td')

    # Extract the state name from the first column, which contains the state abbreviation and name
    # Strip any extra whitespace from the state name
    state = cols[0].text.strip()

    # Extract the score from the second column, which contains the state score as a percentage
    # Strip any extra whitespace from the score
    score = cols[1].text.strip()

    # Print the state name and score as a formatted string

