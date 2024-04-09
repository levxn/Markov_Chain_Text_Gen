from collections import defaultdict

def generate_markov_chain(text):
    markov_chain = defaultdict(list)
    for i in range(len(text) - 2):
        current_sequence = text[i+1]
        next_word_index = i + 2
        if next_word_index < len(text): 
            next_word = text[next_word_index] 
            markov_chain[current_sequence].append(next_word)

    return markov_chain