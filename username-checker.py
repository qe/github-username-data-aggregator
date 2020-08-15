# Two-Letter Username Availability Checker by @ismodes

# Choose whichever website to scrape
rootURL = 'https://github.com/'

# Requests code from webpage
import requests

# BeautifulSoup4 library
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', bs4])
from bs4 import BeautifulSoup

# All 676 permutations of two letters in a list
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

# Iterate



# BeautifulSoup scrape content and set Boolean depending on if there

# create custom delays to slow down web scraping to prevent being blocked (ask about custom delays in webscraping in StackOverflow)
# [EXPLAIN HOW YOU HAVE LOOKED BUT COULDNT FIND HOW TO CUSTOM DELAY] Im not looking necessarily looking for a code specific response, but rather for someone to point me in the right direction of what  

# save into csv with the following columns: (user, boolean)









print(attached)

# Goal 1: check GitHub username availability (if it loads a normal usernamePage  OR  a 404notFound/Other)
# Goal 2: check when each of the two letter usernames were created
#
#
# x1. Generate list of all 256 permutations of two letters
# x2. Append to github root domain 'https://github.com/'
# 3. CHECK STACKOVERFLOW FOR HOW TO ITERATE
