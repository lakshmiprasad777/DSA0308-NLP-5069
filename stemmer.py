import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
porter_stemmer = PorterStemmer()
words = ["running", "ran", "runs", "runner", "easily", "fairly", "fairness"]
stemmed_words = [porter_stemmer.stem(word) for word in words]
for word, stemmed_word in zip(words, stemmed_words):
    print(f"{word}: {stemmed_word}")
