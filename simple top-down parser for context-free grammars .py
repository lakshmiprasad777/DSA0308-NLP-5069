class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
    def parse(self):
        self.current_token_index = 0
        try:
            self.parse_expression()
            if self.current_token_index == len(self.tokens):
                print("Parsing successful!")
            else:
                print("Parsing failed: Unexpected tokens remaining.")
        except Exception as e:
            print("Parsing failed:", e)
    def parse_expression(self):
        self.parse_term()
        while self.match("+"):
            self.consume("+")
            self.parse_term()
    def parse_term(self):
        self.parse_factor()
        while self.match("*"):
            self.consume("*")
            self.parse_factor()
    def parse_factor(self):
        if self.match("("):
            self.consume("(")
            self.parse_expression()
            self.consume(")")
        elif self.match("num"):
            self.consume("num")
        else:
            raise Exception("Expected '(' or 'num'")
    def match(self, expected_token):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index] == expected_token
        else:
            return False
    def consume(self, expected_token):
        if self.match(expected_token):
            self.current_token_index += 1
        else:
            raise Exception(f"Expected '{expected_token}' but found '{self.tokens[self.current_token_index]}'")
tokens = ["num", "+", "num", "*", "num"]
parser = Parser(tokens)
parser.parse()
