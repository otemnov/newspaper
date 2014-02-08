import os

import nltk

from flask import (Flask, request, Response, json)

from newspaper import Article


app = Flask(__name__)


@app.route('/')
def read_newspaper():
    url = request.args.get('url', '')
    if url:
        a = Article(url, image_dimension_ration=3, keep_article_html=True)
        a.download()
        a.parse()
        a.nlp()
        json_string = json.dumps(
            dict(top_image=a.top_image, text=a.article_html, title=a.title, summary=a.summary, images=a.images,
                 movies=a.movies),
            ensure_ascii=False,
            indent=None if request.is_xhr else 2)
        return Response(json_string, mimetype='application/json')
    return Response()


if __name__ == '__main__':
    nltk.data.path.append('./nltk_data/')
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)