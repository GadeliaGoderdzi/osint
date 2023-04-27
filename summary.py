import nltk
import spacy
import locationtagger
from textblob import TextBlob
from newspaper import Article

#nltk downloads
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')


def spy(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    #Text Summery
    print(f'Title: {article.title}')
    print(f'Authors: {article.authors}')
    print(f'Publication Date: {article.publish_date}')
    print(f'Title: {article.summary}')

    #Sentiment or polarity
    analysis = TextBlob(article.text)
    print(analysis.polarity)

    #Locations
    
    place_entity = locationtagger.find_locations(text = article.text)
  
    # getting all countries
    print("The countries in text : ")
    print(place_entity.countries)
 
    # getting all states
    print("The states in text : ")
    print(place_entity.regions)
 
    # getting all cities
    print("The cities in text : ")
    print(place_entity.cities)


