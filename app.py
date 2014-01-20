import os
from flask import Flask
from flask import request
from flask import jsonify
from newspaper import Article


app = Flask(__name__)

@app.route('/')
def hello():
    url = request.args.get('url', '')
    a = Article(url)
    a.download()
    a.parse()
    return jsonify(top_image = a.top_image, text = a.text, title = a.title)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)