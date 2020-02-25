from flask import Flask
from flask_restplus import Api
from .resources import setup_resources


def create_app():
    app = Flask(__name__)
    api = Api(app)
    setup_resources(api)
    return app
