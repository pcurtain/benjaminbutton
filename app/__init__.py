from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from . import views


bootstrap = Bootstrap()
appviews = views.appviews


def create_app(config_name):
    benj = Flask(__name__)
    benj.config.from_object(config[config_name])
    config[config_name].init_app(benj)

    bootstrap.init_app(benj)
    benj.register_blueprint(appviews)

    return benj
