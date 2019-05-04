# from flask import Blueprint
# web = Blueprint('web',__name__)
from flask import render_template

from app.web.blueprint import web


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'),404

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish