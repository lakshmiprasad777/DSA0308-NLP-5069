import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
def morphological_analysis(text):
    words = word_tokenize(text)
    porter = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed_words = [porter.stem(word) for word in words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return stemmed_words, lemmatized_words
text = "The quick brown foxes are jumping over the lazy dogs"
stemmed, lemmatized = morphological_analysis(text)
print("Original text:", text)
print("\nStemmed words:", stemmed)
print("Lemmatized words:", lemmatized)
