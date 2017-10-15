
from html.parser import HTMLParser
from nltk import word_tokenize

tags = ["p", "h1"]
attributes = ["class", "id"]
values = ["story-body-text story-content", "headline"]

# This class getData() method will return tokenized set of words fromt he article given

class MyHTMLFilter(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.setting = 0
		self.stack = []
		self.justFound = False
		self.printedData = False
		self.information = ""
		self.headline = ""

	def handle_starttag(self, tag, attrs):
		if tag in tags:
			if len(attrs) == 0:
				return
			for name, value in attrs:
				if name in attributes and value in values:
					self.stack.append((tag, value))
					self.justFound = True
					break
			if not self.justFound:
				return
			self.justFound = False

	def handle_endtag(self, tag):
		if len(self.stack) == 0:
			return
		if tag in tags and self.stack[len(self.stack) - 1][0] == tag:
			if self.printedData:
				self.printedData = False
			self.stack.pop()

	def handle_data(self, data):
		message = data.strip()

		if message.isspace():
			return
		if len(self.stack) > 0:
			if (self.stack[len(self.stack) - 1][0] == "h1"):
				self.headline = data
			self.information += message + " "

	def getData(self):
		return word_tokenize(self.information)

	def getHeadline(self):
		return self.headline
