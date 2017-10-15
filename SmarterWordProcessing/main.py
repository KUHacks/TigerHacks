import ParseFunctions
import SentenceFunctions
import urllib.request
import re
from nltk import tokenize

urls = ["https://www.nytimes.com/2017/10/02/us/donate-blood-las-vegas.html","https://www.nytimes.com/2017/10/03/us/las-vegas-gunman.html","https://www.nytimes.com/2017/10/10/us/shift-in-las-vegas-timeline-raises-questions-about-police-response.html","https://www.nytimes.com/2017/10/09/us/jesus-campos-las-vegas-shooting.html","https://www.nytimes.com/2017/10/09/us/joseph-lombardo-sheriff-las-vegas.html","https://www.nytimes.com/2017/10/02/us/las-vegas-mass-shooting-weapons.html","https://www.nytimes.com/2017/10/07/us/stephen-paddock-vegas.html"]

exp = '(\d.*(killed|dead|injured))'
regExp = re.compile(exp)

file = open('KeywordsTest.txt', 'w')
file.write("Test for Regular expression: ")

file.write(" on 7 articles\n\n\n")

for url in urls:
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()

	fullhtml = mybytes.decode("utf8")
	parser = ParseFunctions.MyHTMLFilter() # 0 for NYTimes

	parser.feed(fullhtml)

	data = parser.getData()

	sentences = tokenize.sent_tokenize(data)

	file.write(url + "\n\n")
	for sent in sentences:
		regExp.search(sent):
			#for item in SentenceFunctions.cleanSentence(sent):
			#	file.write(item + " ")
			file.write(sent + "\n")

	file.write("\n\n")