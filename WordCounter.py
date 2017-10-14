from html.parser import HTMLParser
import urllib.request
import re
import nltk


urls = ["https://www.nytimes.com/2017/10/02/us/donate-blood-las-vegas.html","https://www.nytimes.com/2017/10/09/us/jesus-campos-las-vegas-shooting.html","https://www.nytimes.com/interactive/2017/10/04/us/vegas-shooting-hotel-room.html","https://www.nytimes.com/video/us/100000005473223/las-vegas-shooting-guns.html","https://www.nytimes.com/2017/10/10/us/shift-in-las-vegas-timeline-raises-questions-about-police-response.html"]

names = ["id", "class"]
tags = ["h1", "p"]
tagref = ["Headline: ", "Story body: "]
ids = [["headline"],["story-body-text story-content"]]

badwords = ["the","on","a","to","of","and","in","were","at","that","has","was","not"]

keywords = ["claim", "happen"]

regexp = re.compile('\$\d*')

totals = dict()

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
			tagIndex = tags.index(self.current[len(self.current) - 1][0])

			#if tagIndex == 0 or any(subs in message for subs in keywords) or hasNumbers(message): # is a headline, or contains claim
			

			# Let's test regular expressions
			#if regexp.search(message):
			words = message.split()
			for word in words:
				if word in badwords:
					continue
				if word in totals:
					totals[word] += 1
				else:
					totals[word] = 1
				if word in counts:
					counts[word] += 1
				else:
					counts[word] = 1
			self.printedData = True
			#print(tagref[tagIndex], message)

# instantiate the parser and fed it some HTML

file = open('output.txt', 'w')

for url in urls:
	counts = dict()
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()


	mystr = mybytes.decode("utf8")
	fp.close()

	print("Page read. Attempting to parse\n\n\n")
	parser = MyHTMLFilter()
	parser.feed(mystr)


	counts_sorted = sorted(counts, key=counts.get, reverse=True)
	i = 0
	file.write("Article: " + url + "\n\n")
	if len(counts) == 0:
		file.write("Couldn't read from this page format")
	for r in counts_sorted:
		#print(r + ": \t" + str(counts[r]))
		file.write(r)
		for x in range(0, 4 - len(r) // 4):
			file.write("\t")
		file.write(str(counts[r]) + "\n")
		i += 1
		if i > 19:
			break
	file.write("\n\n\n")

file.write("\n\n\nTotals\n\n")

totals_sorted = sorted(totals, key=totals.get, reverse=True)
i = 0
for r in totals_sorted:
		#print(r + ": \t" + str(counts[r]))
		file.write(r)
		for x in range(0, 4 - len(r) // 4):
			file.write("\t")
		file.write(str(totals[r]) + "\n")
		i += 1
		if i > 19:
			break