import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer, PorterStemmer, SnowballStemmer
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
not_usefull = set(stopwords.words('english'))
sia = SentimentIntensityAnalyzer()
conjunctions = {
    "but",
    "however",
    "although",
    "though",
    "even though",
    "still",
    "yet"
    "despite",
    "on the other hand",
    "instead"
}

def get_sentiment_vader(text):
    text = text.lower()

    for conjunction in conjunctions:
        if conjunction in text:
            before, after = text.split(conjunction, 1)

            before_score = sia.polarity_scores(before)['compound']
            after_score = sia.polarity_scores(after)['compound']

            print(f"before: {before_score}")
            print(f"after: {after_score}")
            score = 0.2 * before_score + 0.8 * after_score
            break
    else:
        words = word_tokenize(text)
        words = [word for word in words if word.lower() not in not_usefull]
        words = [WordNetLemmatizer().lemmatize(word) for word in words]
        words = [word for word in words if word.isalpha()]
        cleaned_text = " ".join(words)
        print(cleaned_text)

        score = sia.polarity_scores(cleaned_text)['compound']

    return round((score + 1) * 5, 1)