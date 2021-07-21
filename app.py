from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    return response

@app.route('/category/', methods=['GET', 'POST'])
def category_list():
    category_url = "https://api.chucknorris.io/jokes/categories"
    cat_list = requests.get(category_url).json()
    return jsonify(cat_list)


if __name__ == '__main__':
    app.debug = True
    app.run()
