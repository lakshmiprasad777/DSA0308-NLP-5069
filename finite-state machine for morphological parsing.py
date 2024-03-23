class FSM:
    def __init__(self):
        self.transitions = {'start': {'c': 'p1', 'v': 'p2'}, 'p1': {'c': 'p1', 'v': 'p1'}, 'p2': {'c': 'p2', 'v': 'p2'}}
        self.current_state = 'start'
    def transition(self, char_type):
        self.current_state = self.transitions[self.current_state].get(char_type, 'start')
    def pluralize(self, word):
        return word + ('s' if word[-1].lower() in 'aeiou' else 'es')
nouns = ['dog', 'cat', 'box', 'church', 'baby']
fsm = FSM()
for noun in nouns:
    fsm.current_state = 'start'
    plural_form = fsm.pluralize(noun)
    print(f"{noun} -> {plural_form}")
