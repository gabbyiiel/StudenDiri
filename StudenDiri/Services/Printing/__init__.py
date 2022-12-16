from flask import Blueprint

printing = Blueprint('printing', __name__)

from . import routes