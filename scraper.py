# Step 1: Import libraries
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])
from bs4 import BeautifulSoup

import requests
import csv                                    # OPTIONAL: Import if you want to save the data to CSV format

print()
# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')



# Step 2: Extract HTML from source using the 'requests.get()' function and access as attribute
source = requests.get('http://coreyms.com').text



# Step 3: Convert source code into a BeautifulSoup Object called 'soup,' which represents the document as a nested data structure
soup = BeautifulSoup(source, 'lxml')



# OPTIONAL: Open CSV file (if you want to save output into CSV format)
csvFileOpen = open('scraped.csv', 'w')
csvWriter = csv.writer(csvFileOpen)
csvWriter.writerow(['headline', 'summary', 'ytLink'])



# Step 4: Extract highest relevant parent from soup (in this case we are focusing on the articles and their parts/children)
# article = soup.find('article')
# print(article.prettify())
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vidURL = article.find('iframe', class_='youtube-player')['src']
        # print(vidURL)

        # Split up url string based on forward slashes and then on question marks (ID is in between a slash and question mark)
        vidID = vidURL.split('/')[4].split('?')[0]
        # print(vidID)

        ytLink = 'https://youtube.com/watch?v={}'.format(vidID)

    except TypeError as e:
        ytLink = None

    print(ytLink)
    print()
    csvWriter.writerow([headline, summary, ytLink])    # OPTIONAL: Import if you want to save the data to CSV format
csvFileOpen.close()                                    # OPTIONAL: Import if you want to save the data to CSV format
