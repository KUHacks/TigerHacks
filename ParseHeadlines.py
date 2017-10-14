from html.parser import HTMLParser
import urllib.request
import time

# Useful for working with dynamically generated html
from bs4 import BeautifulSoup
from selenium import webdriver

def parse_headlines(topic):
    print("Attempting to open URL")
    #url = "https://www.nytimes.com/2017/10/06/us/las-vegas-shooting.html"
    url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection=U.S.&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=article#/puppies"

    # Working with dynamically generated html
    browser = webdriver.PhantomJS(executable_path=r"/Users/twalen/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs")
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
    topic_parts = topic.split(' ') # comma seperates if we must

    for i in range(0, len(topic_parts)):
        valid_topics = valid_topics + list(filter(lambda x: topic_parts[i] in x[0], titles))

    for i in range(0, len(valid_topics)):
        print(valid_topics[i])

    print("\n\nEnding\n\n")
# Testing
parse_headlines("The")
parse_headlines("The Puppies")
