<<<<<<< HEAD
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import csv\n",
    "\n",
    "# Step 1: Send a GET request to the website\n",
    "url = 'https://www.govtrack.us/congress/bills/subjects/environmental_protection/6038#sort=introduced_date&congress=116'\n",
    "response = requests.get(url)\n",
    "\n",
    "# Step 2: Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    print('Request successful')\n",
    "else:\n",
    "    print(f'Request failed with status code {response.status_code}')\n",
    "    exit()\n",
    "\n",
    "# Step 3: Parse the HTML content of the website using BeautifulSoup\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Step 4: Find the main table containing the bill information\n",
    "bill_table = soup.find('table', {'id': 'bill_list'})\n",
    "\n",
    "# Step 5: Check if the table was found\n",
    "if bill_table is None:\n",
    "    print('Bill table not found')\n",
    "    exit()\n",
    "\n",
    "# Step 6: Create a list to store the bill information\n",
    "bill_info = []\n",
    "\n",
    "# Step 7: Loop through each row of the table and extract the relevant information\n",
    "for row in bill_table.find_all('tr')[1:]:\n",
    "    columns = row.find_all('td')\n",
    "    bill_number = columns[0].text.strip()\n",
    "    bill_title = columns[1].text.strip()\n",
    "    introduced_date = columns[2].text.strip()\n",
    "    sponsor = columns[3].text.strip()\n",
    "    status = columns[4].text.strip()\n",
    "\n",
    "    # Step 8: Add the extracted information to the list\n",
    "    bill_info.append({\n",
    "        'bill_number': bill_number,\n",
    "        'bill_title': bill_title,\n",
    "        'introduced_date': introduced_date,\n",
    "        'sponsor': sponsor,\n",
    "        'status': status\n",
    "    })\n",
    "\n",
    "# Step 9: Write the extracted information to a CSV file\n",
    "filename = 'environmental_protection_bills.csv'\n",
    "with open(filename, 'w', newline='') as csvfile:\n",
    "    fieldnames = ['bill_number', 'bill_title', 'introduced_date', 'sponsor', 'status']\n",
    "    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)\n",
    "\n",
    "    # Step 10: Write the header row to the CSV file\n",
    "    writer.writeheader()\n",
    "\n",
    "    # Step 11: Loop through the list and write each row to the CSV file\n",
    "    for bill in bill_info:\n",
    "        writer.writerow(bill)\n",
    "\n",
    "# Step 12: Print the number of extracted bills and the name of the output file\n",
    "print(f'{len(bill_info)} bills extracted and written to {filename}')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.13 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "c4ba7e12f488ae6c3986849fa75f5c338a09f55952d1cca0020d27ad7cf9ffa3"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
=======
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

>>>>>>> 5b5a261 (scrape)
