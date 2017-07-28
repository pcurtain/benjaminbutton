from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

print(__name__)

appviews = Blueprint('views', __name__, template_folder='templates')

@appviews.route('/', defaults={'page': 'index'})
@appviews.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        raise
        # abort(404)
