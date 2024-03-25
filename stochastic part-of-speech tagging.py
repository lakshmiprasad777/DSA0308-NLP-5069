import nltk
from collections import defaultdict
class SimpleStochasticPOSTagger:
    def __init__(self, corpus):
        self.word_tag_counts = defaultdict(lambda: defaultdict(int))
        self.tag_counts = defaultdict(int)
        self.train(corpus)
    def train(self, corpus):
        for sentence in corpus:
            for word, tag in sentence:
                self.word_tag_counts[word][tag] += 1
                self.tag_counts[tag] += 1
    def tag(self, sentence):
        tagged_sentence = []
        for word in sentence:
            probabilities = {tag: self.word_tag_counts[word][tag] / self.tag_counts[tag] for tag in self.word_tag_counts[word]}
            best_tag = max(probabilities, key=probabilities.get)
            tagged_sentence.append((word, best_tag))
        return tagged_sentence
training_corpus = [
    [("The", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN"), ("jumps", "VBZ"), ("over", "IN"), ("the", "DT"), ("lazy", "JJ"), ("dog", "NN")],
    [("The", "DT"), ("lazy", "JJ"), ("dog", "NN"), ("barks", "VBZ"), ("loudly", "RB")]
]
tagger = SimpleStochasticPOSTagger(training_corpus)
test_sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = tagger.tag(test_sentence)
print("Tagged Sentence:")
print(tagged_sentence)
