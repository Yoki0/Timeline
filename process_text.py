import pandas as pd


def process_document(doc):
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    import string

    # Convert text to Lowercase
    lowered_doc = doc.lower()

    # Remove Punctuation
    removed_pun = lowered_doc.translate(str.maketrans('', '', string.punctuation))

    # Remove Stopwords
    text_tokens = word_tokenize(removed_pun)
    stop_words = set(stopwords.words('english'))

    stopped_doc = ' '.join(word for word in text_tokens if word not in stop_words)

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    text_tokens = word_tokenize(stopped_doc)
    lemmatized_doc = ' '.join(lemmatizer.lemmatize(word) for word in text_tokens)

    return lemmatized_doc

