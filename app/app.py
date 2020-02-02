# app.py

from .Translate import process_text
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return process_text("Hello world", "en", "es")


# Accept a POST request to translate text using AWS Translate.
@app.route('/translate_text', methods=["POST"])
def translate_text():
    data = request.get_json()
    translated_text = process_text(data['textToTranslate'], "en", "es")
    return jsonify({'textToTranslate': translated_text})


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
