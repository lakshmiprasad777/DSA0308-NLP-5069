class TransformationBasedTagger:
    def __init__(self, transformation_rules):
        self.transformation_rules = transformation_rules
    def tag(self, sentence):
        tagged_sentence = []
        for i, (word, _) in enumerate(sentence):
            for rule in self.transformation_rules:
                if rule.condition(sentence, i):
                    tagged_sentence.append((word, rule.tag))
                    break
            else:
                tagged_sentence.append((word, 'NN'))
        return tagged_sentence
class TransformationRule:
    def __init__(self, condition, tag):
        self.condition = condition
        self.tag = tag
transformation_rules = [
    TransformationRule(lambda sentence, i: sentence[i][0].endswith('ing'), 'VBG'), 
    TransformationRule(lambda sentence, i: sentence[i][0].endswith('ed'), 'VBD'),    
    TransformationRule(lambda sentence, i: sentence[i][0].isdigit(), 'CD'),           
]
sentence = [("He", None), ("is", None), ("running", None), ("late", None), ("because", None), ("he", None), ("has", None), ("missed", None), ("the", None), ("train", None)]
tagger = TransformationBasedTagger(transformation_rules)
tagged_sentence = tagger.tag(sentence)
print("Tagged Sentence:")
print(tagged_sentence)
