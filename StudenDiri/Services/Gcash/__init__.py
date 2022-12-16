from flask import Blueprint

gcash = Blueprint('gcash', __name__)

from . import routes