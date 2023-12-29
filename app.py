from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/about/', methods=['GET'])
def about():
    return jsonify({
        'gender': 'male',
        'github_url': 'https://github.com/eedriz99',
        'name': 'Akinsola Idris'
    })


if __name__ == '__main__':
    app.run()
