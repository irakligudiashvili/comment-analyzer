from flask import Flask, render_template, request, redirect, url_for
from menu import menu
from sentiment import get_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    items = menu

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
            rating = get_sentiment(text)
            item['comments'].append({"text": text, "rating": rating})
        return redirect(url_for('comments', item_id=item_id))

    return render_template("comments.html", item=item)

@app.route('/test_sentiment')
def test_sentiment():
    get_sentiment("This is a wonderful dish!")
    return "check console"

if __name__ == "__main__":
    app.run(debug=True, port=5050)