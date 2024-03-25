import re
class RuleBasedPOSTagger:
    def __init__(self):
        self.patterns = [
            (r'\b(?:a|an|the)\b', 'DT'),         
            (r'\b(?:this|that|these|those)\b', 'DT'),  
            (r'\b(?:is|am|are|was|were)\b', 'VB'),     
            (r'\b(?:has|have|had)\b', 'VB'),           
            (r'\b(?:do|does|did)\b', 'VB'),            
            (r'\b(?:I|you|he|she|it|we|they)\b', 'PRP'),  
            (r'\b(?:my|your|his|her|its|our|their)\b', 'PRP$'),  
            (r'\b(?:am|is|are|was|were)\b', 'VBP'),   
            (r'\b(?:go|goes|went|gone|going)\b', 'VB'),  
            (r'\b(?:good|bad|nice|great)\b', 'JJ'),    
            (r'\b(?:quick|brown|lazy|red)\b', 'JJ'),  
            (r'\b(?:over|on|in|at|by|with)\b', 'IN'), 
            (r'\b(?:and|or|but)\b', 'CC'),            
            (r'\b(?:of|to|for|with|about|as|into|like|through)\b', 'IN'),  
            (r'\b(?:.\w+)\b', 'NN'),                 
            (r'\b(?:.\w+ly)\b', 'RB'),              
            (r'\b(?:[0-9]+)\b', 'CD'),               
        ]
    def tag(self, text):
        tagged_text = []
        for word in text.split():
            for pattern, tag in self.patterns:
                if re.match(pattern, word):
                    tagged_text.append((word, tag))
                    break  
            else:
                tagged_text.append((word, 'NN')) 
        return tagged_text
    tagger = RuleBasedPOSTagger()
text = "The quick brown fox jumps over the lazy dog."
tagged_text = tagger.tag(text)
print("Tagged Text:")
print(tagged_text)
