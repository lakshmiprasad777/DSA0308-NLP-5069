import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
conversation = [
    "Hello there! How are you doing today?",
    "I'm doing great, thanks for asking.",
    "Can you help me with my homework?",
    "Sure, I'd be happy to help. What do you need assistance with?",
    "I'm stuck on this math problem.",
    "Alright, let me take a look.",
]
for i, utterance in enumerate(conversation):
    sentences = sent_tokenize(utterance)
    for j, sentence in enumerate(sentences):
        words = word_tokenize(sentence)
        if "?" in words:
            dialog_act = "question"
        else:
            dialog_act = "statement"
        print(f"Utterance {i + 1}, Sentence {j + 1}: {dialog_act.capitalize()} - {sentence}")
