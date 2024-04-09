import random
from find_match import find_similar_word

def generate_text(markov_chain, seed_word=None, length=50, word_embeddings=None, similarity_threshold=0.5, randomness_factor=0.7):
    generated_text = []
    prev_words = []

    if seed_word:
        current_sequence = seed_word
        generated_text.append(seed_word)
    else:
        current_sequence = random.choice(list(markov_chain.keys()))
        generated_text.extend(current_sequence.split())

    for _ in range(length - 1):
        next_word_options = markov_chain[current_sequence]

        # Remove previously selected words from options
        next_word_options = [word for word in next_word_options if word not in prev_words]

        if not next_word_options:
            break

        if word_embeddings:
            if seed_word:
                next_word = find_similar_word(seed_word, next_word_options, word_embeddings, similarity_threshold, randomness_factor)
            else:
                next_word = find_similar_word(current_sequence, next_word_options, word_embeddings, similarity_threshold, randomness_factor)
        else:
            next_word = random.choice(next_word_options)

        generated_text.append(next_word)
        prev_words.append(next_word)
        if len(prev_words) > 3:
            prev_words.pop(0)

        if not seed_word:
            current_sequence = ' '.join(generated_text[-3:])

    return ' '.join(generated_text)