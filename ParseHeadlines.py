from html.parser import HTMLParser
import urllib.request
import time

# Useful for working with dynamically generated html
# You'll need to download both Selenium and BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
nyt_base_url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection=U.S.&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=article#/"
cnn_base_url = "http://www.cnn.com/search/?size=10&q="

class Topic:
    def __init__(self, topic, depth):
        self.topic = topic # Each instantiation has its own topic
        self.depth = depth # Depth of search on each news source
        self.articles = [] # Initialized as an empty list that will be populated by each news source

    def get_web_driver(self):
        return webdriver.PhantomJS(executable_path=r"/Users/twalen/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs") # CHANGE IF ON A DIFFERENT MACHINE

    def get_nyt_articles(self, url):
        topic_parts = self.topic.split(' ') # comma seperates if we must

        # Working with dynamically generated html
        browser = self.get_web_driver()
        browser.get(url)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        conts = soup.find_all('h3') # gets a list of tags
        titles = []

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

    def get_cnn_articles(self, url):
        topic_parts = self.topic.split(' ') # comma seperates if we must

        # Working with dynamically generated html
        browser = self.get_web_driver()
        browser.get(url)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        a = soup.select('.cnn-search__result-headline') # gets a list of anchor tags with the info
        titles = []

        # Let's get those titles and their urls
        for i in range(0, len(a)):
            loc = a[i].a
            if loc:
                if loc:
                    temp = (loc.string, loc['href'])
                    titles.append(temp)

        # now we can determine if we have good input
        valid_topics = []

        for i in range(0, len(topic_parts)):
            valid_topics = valid_topics + list(filter(lambda x: topic_parts[i] in x[0], titles))

        return valid_topics


    def get_arcticles(self):
        query = self.topic.replace(' ', '%20')

        # get nyt articles
        nyt_query_url = nyt_base_url + query + '/'

        # concat results from a parse on a site
        for i in range(0, self.depth):
            # query
            self.articles = self.articles + self.get_nyt_articles(nyt_query_url)
            # build next url
            next_page = i + 1
            nyt_query_url = nyt_query_url + str(next_page) + '/'

        # get cnn articles
        cnn_query_url = cnn_base_url + query

        # concat results from a parse on a sit
        for i in range(0, self.depth):
            # query
            self.articles = self.articles + self.get_cnn_articles(cnn_query_url)
            # build next url
            next_page = i + 1
            next_start_point = 10 * next_page # gets us the display query
            cnn_query_url = cnn_query_url + '&from=' + str(next_start_point) + '&page=' + str(next_page)


# Testing
my_topic = "The"
d = 5
print("Searching for articles about " + my_topic + " on " + str(d) + " pages...")
top = Topic("The", 5)
top.get_arcticles()

for i in range(0, len(top.articles)):
    print(top.articles[i])
