from html.parser import HTMLParser
import urllib.request
import time

# Useful for working with dynamically generated html
# You'll need to download both Selenium and BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
base_url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection=U.S.&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=article#/"

class Topic:
    def __init__(self, topic, depth):
        self.topic = topic # Each instantiation has its own topic
        self.depth = depth # Depth of search on each news source
        self.articles = [] # Initialized as an empty list that will be populated by each news source

    def get_nyt_articles(self, url):
        topic_parts = self.topic.split(' ') # comma seperates if we must

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

        # now we can determine if we have good input
        valid_topics = []

        for i in range(0, len(topic_parts)):
            valid_topics = valid_topics + list(filter(lambda x: topic_parts[i] in x[0], titles))

        return valid_topics

    def get_arcticles(self):
        query = self.topic.replace(' ', '%20')
        query_url = base_url + query + '/'

        # concat results from a parse
        for i in range(0, self.depth):
            # query
            self.articles = self.articles + self.get_nyt_articles(query_url)
            # build next url
            next_page = i + 1
            query_url = query_url + str(next_page) + '/'




# Testing
my_topic = "The"
d = 5
print("Searching for articles about " + my_topic + " on " + str(d) + " pages...")
top = Topic("The", 5)
top.get_arcticles()

for i in range(0, len(top.articles)):
    print(top.articles[i])
