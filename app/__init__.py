# app/__init__.py
import os
from flask import Flask
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name.strip()])
    app.config.from_pyfile('../config.py')

    from app.translate import bp as translate_bp
    app.register_blueprint(translate_bp)

    return app


config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

# from app import routes