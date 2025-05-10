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

def get_sentiment(text):
    words = word_tokenize(text)

    words = [word for word in words if word.lower() not in not_usefull]

    words = [WordNetLemmatizer().lemmatize(word) for word in words]

    words = [word for word in words if word.isalpha()]

    cleaned_text = " ".join(words)
    print(cleaned_text)

    scores = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    print(scores)
    return round((scores['compound'] + 1) * 5, 1)