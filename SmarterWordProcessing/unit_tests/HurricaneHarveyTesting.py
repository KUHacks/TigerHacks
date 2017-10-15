import ParseFunctions
import SentenceFunctions
import urllib.request
import re
from nltk import tokenize

urls = ["https://www.nytimes.com/2017/08/30/us/hurricane-center-timeline.html","https://www.nytimes.com/2017/08/26/us/hurricane-harvey-forecast-texas-louisiana.html","https://www.nytimes.com/2017/08/23/us/tropical-storm-harvey-gulf.html","https://www.nytimes.com/2017/09/11/reader-center/hurricane-harvey-teacups.html","https://www.nytimes.com/2017/09/17/us/harvey-port-arthur-mayor.html","https://www.nytimes.com/2017/09/08/theater/alley-theater-harvey-houston.html","https://www.nytimes.com/2017/09/16/us/hurricane-harvey-houston-wilma-ellis.html"]

exp = '\d\d:\d\d'
exp2 = '(\d.*(killed|dead|injured))'
exp3 = 'killed \d*|\d\d* (victim|people)'
regExp = re.compile(exp)
regExp2 = re.compile(exp2)
regExp3 = re.compile(exp3)

punctuation = ["“", "”", "’", "—"]

file = open('Harvey.txt', 'w')
file.write("Test for Regular expressions with hurricane harvey this time: ")
file.write(exp)
file.write(" and ")
file.write(exp2)
file.write(" on 7 articles\n\n\n")
file.write("We are trying to find general information about the incident at hand. That is, specific information regarding what happened\n\n\n")

count = 0
cleanedSentences = []

for url in urls:
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()

	fullhtml = mybytes.decode("utf8")
	parser = ParseFunctions.MyHTMLFilter()

	parser.feed(fullhtml)

	data = parser.getData()

	sentences = tokenize.sent_tokenize(data)


	file.write(url + "\n\n")
	for sent in sentences:
		cleanedSentences.append(SentenceFunctions.cleanSentence(sent))
		if regExp.search(sent) or regExp2.search(sent) or regExp3.search(sent):
			file.write(sent + "\n")

	file.write("\n\n")

wordCounts = dict()

for sentArr in cleanedSentences:
	for item in sentArr:
		if item in wordCounts:
			wordCounts[item] += 1
		else:
			wordCounts[item] = 1

file.write("WORD COUNTS > 2\n---------------\n\n")
outputCount = 0
for word in sorted(wordCounts, key=wordCounts.get, reverse=True):
	#if (wordCounts[word] < 2):
		#continue
	if word in punctuation:
		continue
	if outputCount > 19:
		break
	file.write(word)
	for x in range(0, 5 - len(word) // 4):
		file.write("\t")
	file.write(str(wordCounts[word]))
	file.write("\n")
	outputCount += 1