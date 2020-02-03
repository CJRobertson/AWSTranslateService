#translate/__init__.py
from flask import Blueprint

bp = Blueprint('translate', __name__)

from app.translate import routes


