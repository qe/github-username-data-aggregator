# github-username-data-aggregator
# Custom delay script to not overload the website!!!
# To-Do-List to Add: 'join date', 'amount of repositories',

# Imports 'requests' module to allow HTTP requests
import requests

# Imports the 'time' module
import time

# Import randrange function from the 'random' module
from random import randrange

# Assigns the string of the path of the current directory to the variable 'path'
from pathlib import Path
path = str(Path(__file__).parent.absolute())

# Installs BeautifulSoup4, a web scaping library
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', bs4])
from bs4 import BeautifulSoup

# Set the standard root URL for accessing users profiles
rootURL = 'https://github.com/'

# Set the username letter length
# numLetters = int(input('Enter the username letter length you want data on (e.g. 1 --> one-letter handles, 2--> two-letter handles..): '))
numLetters = 1

# Creates a CSV file in the current working directory
import csv
csvLabel = '1LetterGitHubUsernamesTest'
csvName = '/' + csvLabel + '.csv'
# csvName = '/' + input('Name the CSV file with the username data: ') + '.csv'
csvFile = path + csvName
csvFileOpen = open(csvFile, 'w')
csvWriter = csv.writer(csvFileOpen)
csvWriter.writerow(['username', 'availability', 'type', 'location', 'work'])

# Set 'repeat' to 1 for all 26 letters in a list   OR   Set repeat to 2 for all 676 permutations of two-letters in a list
# OR set 'repeat' to 3 for all 17576 permutations of three-letters...
from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = numLetters)]

# Append root URL with keywords representing each user's profile links
def attach(rootURL, keywords):
    attached = []
    for i in keywords:
        bind = []
        bind.append(rootURL)
        bind.append(i)
        attached.append(''.join(bind))
    return attached
attached = attach(rootURL, keywords)

for i in range(len(attached)):
    randomDelay = randrange(11,19)

    theURL = requests.get(attached[i])

    source = requests.get(attached[i],time.sleep(randomDelay)).text
    soup = BeautifulSoup(source, 'lxml')
    # head = soup.find('div', class_='application-main')
    content = soup.find('div', class_='application-main')

    # Default values
    username = None
    Organization = None
    fourOfour = None
    type = None
    availability = False

    # User
    try:
        username = content.find('span', class_='p-nickname vcard-username d-block', itemprop='additionalName').text
        type = 'User'
    except:
        pass

    # Organization
    try:
        print(keywords[i])
        org = content.find('h1', class_='text-gray-dark lh-condensed mb-1 mb-md-2').text
        type = 'Organization'
    except:
        pass

    # Redirect
    try:
        if theURL.url != attached[i]:
            type = 'Redirect'
    except:
        pass

    # 404
    try:
        if (type == None):
            type = '404'
    except:
        pass

    # Availability
    if type == '404':
        availability = True

    # Location
    try:
        location = content.find('span', class_='p-label').text
    except:
        location = None

    # Work
    try:
        work = content.find('span', class_='p-org').text
    except:
        work = None

    print(type)
    csvWriter.writerow([keywords[i], availability, type, location, work])

csvFileOpen.close()
