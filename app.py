import nltk
from textblob import TextBlob
from newspaper import Article

url = "https://indianexpress.com/article/world/israel-palestine-war-live-updates-hamas-gaza-news-today-8977319/"

nltk.download('punkt')

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary : {article.summary}')


analysis = TextBlob(article.text)
print(analysis.polarity)

print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')