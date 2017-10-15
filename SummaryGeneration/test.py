# Let's try to utilize what we have to get a tokenized list of words in the article.

import NYTimesScrape
import urllib.request

req = urllib.request.urlopen("https://www.nytimes.com/2017/10/03/us/las-vegas-gunman.html")
bytestring = req.read()
rawHTML = bytestring.decode("utf8")
req.close()


parser = MyHTMLFilter()
parser.feed(rawHTML)

# Dope. This works