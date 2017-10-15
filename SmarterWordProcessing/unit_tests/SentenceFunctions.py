
from nltk.corpus import stopwords
from nltk import word_tokenize


def cleanSentence(sentence):
	tokens = word_tokenize(sentence)
	stop_words = set(stopwords.words('english'))
	punctuation = [",","."]

	return [w for w in tokens if not w in stop_words and not w in punctuation]
