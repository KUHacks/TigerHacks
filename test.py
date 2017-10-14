from html.parser import HTMLParser
import urllib.request
import time

tags = ["h3"]
ids = ["headline"]

# This is essentially working and pulling headlines from any NYT article
class MyHTMLFilter(HTMLParser):
	current = [] # empty stack
	found = False


	def handle_starttag(self, tag, attrs):
		if tag in tags:
			print("START TAG: ", tag)
			self.current.append(tag)
	def handle_endtag(self, tag):
		if tag in tags:
			print("END TAG: ", tag)
			self.current.pop()
	def handle_data(self, data):
		if data.isspace():
			return
		if len(self.current) > 0:
			print(self.current[len(self.current) - 1], ":   ", data.strip())

# instantiate the parser and fed it some HTML

print("Attempting to open URL")
#url = "https://www.nytimes.com/2017/10/06/us/las-vegas-shooting.html"
url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection=U.S.&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=article#/puppies"
fp = urllib.request.urlopen(url)
print("URL opened. Waiting 5 secs before reading.")
time.sleep(5)

print("Attempting to read page.")

mybytes = fp.read()


mystr = mybytes.decode("utf8")
fp.close()

print("Page read. Attempting to parse")
parser = MyHTMLFilter()
parser.feed(mystr)
