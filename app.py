import os
import nltk
from flask import Flask
from flask import request
from flask import jsonify
from newspaper import Article


app = Flask(__name__)

@app.route('/')
def read_newspaper():
    url = request.args.get('url', '')
    a = Article(url, image_dimension_ration = 3)
    a.download()
    a.parse()
    a.nlp()
    return jsonify(top_image = a.top_image, text = a.text, title = a.title, summary = a.summary, images = a.images, movies = a.movies, meta_data = a.meta_data)

if __name__ == '__main__':
    nltk.data.path.append('./nltk_data/')
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)