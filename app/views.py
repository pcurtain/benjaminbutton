from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound


appviews = Blueprint('views', __name__, template_folder='templates')


@appviews.route('/', defaults={'page': 'index'})
@appviews.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
