import re
import nltk

nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove non-alphanumeric characters
    return text

def preprocess_text(text):
    cleaned_text = clean_text(text)
    sentences = nltk.sent_tokenize(cleaned_text)
    tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return sentences, tokens
