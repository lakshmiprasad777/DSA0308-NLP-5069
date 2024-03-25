import random
text = "The quick brown fox jumps over the lazy dog. The lazy dog barks loudly."
words = text.lower().split()
bigrams = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word in bigrams:
        bigrams[current_word].append(next_word)
    else:
        bigrams[current_word] = [next_word]
start_word = random.choice(list(bigrams.keys()))
generated_text = [start_word]
current_word = start_word
while len(generated_text) < 20:  
    if current_word in bigrams:
        next_word = random.choice(bigrams[current_word])
        generated_text.append(next_word)
        current_word = next_word
    else:
        break
generated_text = ' '.join(generated_text)
print(generated_text)
