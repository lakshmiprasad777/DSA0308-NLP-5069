class PluralFiniteStateMachine:
    def __init__(self):
        self.transitions = {
            'S': {'s': 'S1', 'x': 'S2', 'y': 'S3', 'z': 'S4'},
            'S1': {'': 'ES'},
            'S2': {'': 'ES'},
            'S3': {'': 'ES'},
            'S4': {'': 'ES'},
            'ES': {},
        }
    def pluralize(self, noun):
        state = 'S'
        for letter in noun[::-1]:  
            if letter in self.transitions[state]:
                state = self.transitions[state][letter]
            else:
                return None  
        if state in self.transitions:
            return noun + 'es'  
        else:
            return None  
if __name__ == "__main__":
    fsm = PluralFiniteStateMachine()
    nouns = ['cat', 'box', 'baby', 'buzz']
    for noun in nouns:
        plural = fsm.pluralize(noun)
        if plural:
            print(f"{noun} -> {plural}")
        else:
            print(f"Invalid input: {noun}")
