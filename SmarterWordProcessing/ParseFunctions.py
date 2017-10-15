
from html.parser import HTMLParser

tags = ["h1","p"]
attributes = ["id", "class"]
values = ["headline", "story-body-text story-content"]



class MyHTMLFilter(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.setting = 0
		self.stack = []
		self.justFound = False
		self.printedData = False
		self.information = ""

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
			#if hasNumbers(message) or "happen" in message:
			#tagIndex = tags.index(self.current[len(self.current) - 1][0])
			self.information += message + " "

	def getData(self):
		return self.information
