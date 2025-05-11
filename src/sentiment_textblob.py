# pip install textblob
# python -m textblob.download_corpora

from textblob import TextBlob

def get_sentiment_blob(text):
    text = text.lower()

    if "but" in text:
        before, after = text.split("but", 1)
        before_polarity = TextBlob(before).sentiment.polarity
        after_polarity = TextBlob(after).sentiment.polarity

        score = 0.25 * before_polarity + 0.75 * after_polarity
    else:
        score = TextBlob(text).sentiment.polarity

    print(f"Polarity: {score}")

    return round((score + 1) * 5, 1)