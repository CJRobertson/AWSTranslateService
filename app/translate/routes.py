from app.translateservice import TranslateText
from flask import Flask, request, jsonify
from app.translate import bp
from cerberus import Validator

schema = {
    'textToTranslate': {'type': 'string'},
    'source_lang': {'type': 'string'},
    'dest_lang': {'type': 'string'},
}

valid_schema = Validator(schema)


class InvalidPayload(Exception):
    status_code = 422

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@bp.errorhandler(InvalidPayload)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# Accept a POST request to translate text using AWS Translate.
@bp.route('/translate_text', methods=["POST"])
def translate_text():
    translator = TranslateText()
    data = request.get_json()
    if not valid_schema.validate(data):
        raise InvalidPayload('Malformed JSON', status_code=422)
    return jsonify({'translatedText': translator.process_text(data['textToTranslate'], data['source_lang'], data['dest_lang'])})
