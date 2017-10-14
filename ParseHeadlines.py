from html.parser import HTMLParser
import urllib.request
import time

# Useful for working with dynamically generated html
# You'll need to download both Selenium and BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
base_url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection=U.S.&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=article#/"

# pretty slow method
def parse_headlines(topic, url):
    print("Attempting to open URL")
    #url = "https://www.nytimes.com/2017/10/06/us/las-vegas-shooting.html"

    topic_parts = topic.split(' ') # comma seperates if we must

    # Working with dynamically generated html
    browser = webdriver.PhantomJS(executable_path=r"/Users/twalen/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs") # CHANGE IF ON A DIFFERENT MACHINE
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    conts = soup.find_all('h3') # gets a list of tags
    titles = [] # empty list

    # Let's get those titles and their urls
    for i in range(0, len(conts)):
        temp = conts[i].find('a')
        if temp:
            if temp.string:
                temp = (temp.string, temp['href'])
                titles.append(temp)
                print(temp)

    print("\n\n\n")

    # now we can determine if we have good input
    valid_topics = []

    for i in range(0, len(topic_parts)):
        valid_topics = valid_topics + list(filter(lambda x: topic_parts[i] in x[0], titles))

    for i in range(0, len(valid_topics)):
        print(valid_topics[i])

    print("\n\nEnding\n\n")

# does not gaurd against bad input
def find_articles(topic, depth):
    print("Finding articles about " + topic + " on " + str(depth) + " pages.")
    query = topic.replace(' ', '%20')
    query_url = base_url + query + '/'

    for i in range(0, depth):
        # query
        parse_headlines(topic, query_url)
        # build next url
        next_page = i + 1
        query_url = query_url + str(next_page) + '/'
        print('\n\nPage ' + str(next_page))

# Testing
find_articles("The", 5)
find_articles("The Puppies", 2)
