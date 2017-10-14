
import newspaper

paper = newspaper.build("http://www.cnn.com/")

if paper.size() == 0:
	print("No articles could be found...")
else:
	first_article = paper.articles[0]
	first_article.download()
	print(first_article.summary)