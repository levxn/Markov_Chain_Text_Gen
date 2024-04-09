import pandas as pd
from gensim.models import Word2Vec
from preprocess import preprocess_text
from markov import generate_markov_chain
from gen_text import generate_text  

def main():
    csv_file_path = "abcnews-date-text.csv"
    df = pd.read_csv(csv_file_path)
    text_column_name = 'headline_text'
    all_text = " ".join(df[text_column_name].astype(str))
    preprocessed_text = preprocess_text(all_text)
    # Word2Vec
    word2vec_model = Word2Vec(sentences=[preprocessed_text], vector_size=100, window=5, min_count=1, workers=4)
    #Word Embeddings
    word_embeddings = word2vec_model.wv
    # Markov Chain
    markov_chain = generate_markov_chain(preprocessed_text)
    while True:
        try:
            seed_word = str(input('Enter start word: '))
            length = int(input('Enter word length: '))
            for i in range(20):
                print(str(i+1) + ". ", generate_text(markov_chain, seed_word, length, word_embeddings))
            print()
        except ValueError:
            print("Invalid input. Re-enter")
            continue
        except KeyError:
            print("Start word not found in corpus")
            continue

if __name__ == "__main__":
    main()