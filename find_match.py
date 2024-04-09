import random
import numpy as np

def find_similar_word(current_word, next_word_options, word_embeddings, similarity_threshold, randomness_factor=0.5):
    valid_similarities = []
    valid_words = []
    
    for word in next_word_options:
        if word in word_embeddings:
            similarity = word_embeddings.similarity(current_word, word)
            if similarity > similarity_threshold:
                valid_similarities.append(similarity)
                valid_words.append(word)
    
    if valid_similarities:
        weights = np.array(valid_similarities) / np.sum(valid_similarities)
        weighted_choice = np.random.choice(valid_words, p=weights)
        if np.random.rand() > randomness_factor:
            return weighted_choice
        else:
            return random.choice(next_word_options)
    else:
        return random.choice(next_word_options)