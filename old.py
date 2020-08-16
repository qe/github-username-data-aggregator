
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])

import requests
from bs4 import BeautifulSoup



with open('simple.html') as html_file:          # parses html file
    soup = BeautifulSoup(html_file, 'lxml')     #
#
# print(soup.prettify())                                     # prints out all the html code indented (indented because of prettify method)



# to get FIRST information from a tag --> access it like an attribute
# e.g. if you wanted to grab the FIRST title from the html then access it like an attribute
# match = soup.title.text
# print(match)



# if you want to find a specific tag that IS NOT necessarily the FIRST of its kind in the code then use the 'find' method
# e.g. if you want to grab the div tag that has a class of footer then use the 'find' method and pass in some arguments

individualArticle = soup.find('div', class_='article')
print(individualArticle.text)
print()



for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)


    summary = article.p.text
    print(summary)

    print()











# res = requests.get('https://github.com')
#
# soup = bs4.BeautifulSoup(res.txt, 'lxml')
#
# type(soup)
