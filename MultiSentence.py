from html.parser import HTMLParser
import urllib.request
import re
from nltk import tokenize


urls = ["https://www.nytimes.com/2017/10/02/us/donate-blood-las-vegas.html","https://www.nytimes.com/2017/10/03/us/las-vegas-gunman.html","https://www.nytimes.com/2017/10/10/us/shift-in-las-vegas-timeline-raises-questions-about-police-response.html","https://www.nytimes.com/2017/10/09/us/jesus-campos-las-vegas-shooting.html","https://www.nytimes.com/2017/10/09/us/joseph-lombardo-sheriff-las-vegas.html","https://www.nytimes.com/2017/10/02/us/las-vegas-mass-shooting-weapons.html","https://www.nytimes.com/2017/10/07/us/stephen-paddock-vegas.html"]

names = ["id", "class"]
tags = ["h1", "p"]
tagref = ["Headline: ", "Story body: "]
ids = [["headline"],["story-body-text story-content"]]

regexp = re.compile('(\d.*(killed|dead|injured))')


f = ""

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

# This is essentially working and pulling headlines from any NYT article
class MyHTMLFilter(HTMLParser):
	current = [] # empty stack
	justFound = False
	printedData = False
	


	def handle_starttag(self, tag, attrs):
		if tag in tags:
			if len(attrs) == 0:
				return
			for name, value in attrs:
				if name in names and value in ids[tags.index(tag)]:
					self.current.append((tag, value))
					self.justFound = True
					break
			if not self.justFound:
				return
			#print("START TAG: ", tag)
			self.justFound = False

	def handle_endtag(self, tag):
		if len(self.current) == 0:
			return
		if tag in tags and self.current[len(self.current) - 1][0] == tag:
			#print("END TAG: ", tag)
			if self.printedData:
				#print("\n\n\n")
				self.printedData = False
			self.current.pop()

	def handle_data(self, data):
		message = data.strip()

		if message.isspace():
			return
		if len(self.current) > 0:
			#if hasNumbers(message) or "happen" in message:
			global f
			tagIndex = tags.index(self.current[len(self.current) - 1][0])
			f += message

			

# instantiate the parser and fed it some HTML


file = open('sentences.txt', 'w')

for url in urls:
	f = ""
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()

	mystr = mybytes.decode("utf8")
	fp.close()

	print("Page read. Attempting to parse\n\n")
	parser = MyHTMLFilter()
	parser.feed(mystr)

	sentences = tokenize.sent_tokenize(f)

	file.write(url + "\n\n")

	for sent in sentences:
		if regexp.search(sent):
			file.write(sent + "\n")

	file.write("\n\n\n")