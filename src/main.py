import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from flask import Flask, render_template, request, redirect, url_for
from menu import menu
from sentiment_vader import get_sentiment_vader
from sentiment_textblob import get_sentiment_blob
from storage import save_menu, load_menu

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHART_DIR = os.path.join(BASE_DIR, 'static/charts')
os.makedirs(CHART_DIR, exist_ok=True)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    items = menu

    ratings ={
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    for item in items:
        labels = []
        sizes = []

        ratings = {
            "positive": 0,
            "neutral": 0,
            "negative": 0
        }

        for comment in item['comments']:
            print(comment['rating'])
            if comment['rating'] < 4:
                ratings['negative'] += 1
            elif comment['rating'] >= 4 and comment['rating'] <= 6:
                ratings['neutral'] += 1
            elif comment['rating'] > 6:
                ratings['positive'] += 1

        for x, y in ratings.items():
            labels.append(x)
            sizes.append(y)

        plt.figure()
        plt.pie(sizes, labels=labels)
        chart_path = f"{CHART_DIR}/chart_{item['title']}.png"
        plt.savefig(chart_path)
        plt.close()

    return render_template("index.html", items=items)

@app.route('/test', methods=['POST', 'GET'])
def test():
    return {
        "test": "area"
    }

@app.route('/comments/<int:item_id>', methods=['GET', 'POST'])
def comments(item_id):
    item = next((i for i in menu if i["id"] == item_id), None)

    if request.method == 'POST':
        text = request.form.get('comment')
        if text:
            rating = get_sentiment_vader(text)
            item['comments'].append({"text": text, "rating": rating})
            save_menu(menu)
        return redirect(url_for('comments', item_id=item_id))

    return render_template("comments.html", item=item)

@app.route('/test_sentiment')
def test_sentiment():
    get_sentiment_vader("This is a wonderful dish!")
    return "check console"

if __name__ == "__main__":
    app.run(debug=True, port=5050)