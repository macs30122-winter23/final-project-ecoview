'''
This file is responsible for scraping the bills belonging to Environmental Protection from all U.S. states between the years 2018 and 2021.
'''

import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a GET request to the website
url = 'https://www.govtrack.us/congress/bills/subjects/environmental_protection/6038#sort=introduced_date&congress=116'
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    print('Request successful')
else:
    print(f'Request failed with status code {response.status_code}')
    exit()

# Step 3: Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find the main table containing the bill information
bill_table = soup.find('table', {'id': 'bill_list'})

# Step 5: Check if the table was found
if bill_table is None:
    print('Bill table not found')
    exit()

# Step 6: Create a list to store the bill information
bill_info = []

# Step 7: Loop through each row of the table and extract the relevant information
for row in bill_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    bill_number = columns[0].text.strip()
    bill_title = columns[1].text.strip()
    introduced_date = columns[2].text.strip()
    sponsor = columns[3].text.strip()
    status = columns[4].text.strip()

    # Step 8: Add the extracted information to the list
    bill_info.append({
        'bill_number': bill_number,
        'bill_title': bill_title,
        'introduced_date': introduced_date,
        'sponsor': sponsor,
        'status': status
    })

# Step 9: Write the extracted information to a CSV file
filename = 'environmental_protection_bills.csv'
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['bill_number', 'bill_title', 'introduced_date', 'sponsor', 'status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Step 10: Write the header row to the CSV file
    writer.writeheader()

    # Step 11: Loop through the list and write each row to the CSV file
    for bill in bill_info:
        writer.writerow(bill)

