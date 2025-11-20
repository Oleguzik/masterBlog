from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load articles from JSON file
    with open('articles.json', 'r') as f:
        posts = json.load(f)
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5015, debug=True)