# Github Username Data Aggregator by @qe

# M E T H O D S
# Extract info on active repositories? (bool), has a name? (bool), location (e.g. San Francisco), work (@facebook)

# G O A L S
# Username Availability (e.g. default, 404, or redirect), Average followers for 1-letter/2-letter accounts, MAYBE when the accout joined?, most common locations


# Choose whichever website to scrape
rootURL = 'https://github.com/'

# Requests code from webpage
import requests

# Import CSV library
import csv

# BeautifulSoup4 library
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', bs4])
from bs4 import BeautifulSoup

# Set repeat to 1 for all 26 letters in a list   OR   Set repeat to 2 for all 676 permutations of two letters in a list
from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]

# Format all 676 permutations into website url's for each user
def attach(rootURL, keywords):
    attached = []
    for i in keywords:
        bind = []
        bind.append(rootURL)
        bind.append(i)
        attached.append(''.join(bind))
    return attached
attached = attach(rootURL, keywords)

# Open CSV document
csvFileOpen = open('usernameData.csv', 'w')
csvWriter = csv.writer(csvFileOpen)
csvWriter.writerow(['username', 'availability', 'join date', 'active', 'location', 'work'])

# print(attached.index('https://github.com/qe'))

print(attached.index('https://github.com/yg'))

# print(attached[675])


source = requests.get(attached[2]).text

# source = requests.get('https://github.com/c').text    # for error message

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

try:
    content = soup.find('div', class_='application-main')     # maybe add .text to the end


# csvWriter.writerow([headline, summary, ytLink])
    try:
        # Username
        username = content.find('span', itemprop='additionalName').text
        print(username)

        # REPARAR
        # Availability
        try:
            availability = content.find('img', alt='404 “This is not the web page you are looking for”')
            availability = True
        except:
            availability = False
        print(availability)

        # Join date
        pass

        # Any repos?

        # Location
        try:
            location = content.find('span', class_='p-label').text
        except:
            location = 'Unknown location'
        print(location)

        # Work
        try:
            work = content.find('span', class_='p-org').text
        except:
            work = 'Unknown work'
        print(work)




    except:
        username = 'Link does NOT load to a user'
        print(username)



    # Availability
    # Join date
    # Active check the 'user ha s_ repositories message'







except:
    print('Error in parsing file')



#
# for i in attached:
#     eachUser = requests.get()






# Iterate

# DECIDE if you should structure the iterator or code the soup extractor

# BeautifulSoup scrape content and set Boolean depending on if there


# How to scrape at a reasonable rate
# create custom delays to slow down web scraping to prevent being blocked (ask about custom delays in webscraping in StackOverflow)
# [EXPLAIN HOW YOU HAVE LOOKED BUT COULDNT FIND HOW TO CUSTOM DELAY] Im not looking necessarily looking for a code specific response, but rather for someone to point me in the right direction of what


# save into csv with the following columns: (user, boolean)









# print(attached)                   # prints all permutation








# Goal 1: check GitHub username availability (if it loads a normal usernamePage  OR  a 404notFound/Other)
# Goal 2: check when each of the two letter usernames were created
#
#
# x1. Generate list of all 256 permutations of two letters
# x2. Append to github root domain 'https://github.com/'
# 3. CHECK STACKOVERFLOW FOR HOW TO ITERATE
