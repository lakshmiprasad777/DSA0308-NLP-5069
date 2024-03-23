class FSA:
    def __init__(self):
        self.transitions = {
            'start': {'a': 'found_a', 'b': 'start'},
            'found_a': {'a': 'found_a', 'b': 'found_ab'},
            'found_ab': {'a': 'found_a', 'b': 'start'}
        }
        self.current_state = 'start'
    def transition(self, char):
        if char in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][char]
        else:
            self.current_state = 'start'
    def is_match(self):
        return self.current_state == 'found_ab'
fsa = FSA()
test_strings = ['ab', 'aab', 'ba', 'b', 'abab', 'aba']
for test_string in test_strings:
    for char in test_string:
        fsa.transition(char)
    if fsa.is_match():
        print(f"'{test_string}' matches the pattern.")
    else:
        print(f"'{test_string}' does not match the pattern.")
    fsa.current_state = 'start'
