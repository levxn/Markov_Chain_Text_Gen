import re
import nltk
from nltk.corpus import stopwords

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())
    text = re.sub(r'http\S+', '', text.lower())
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens