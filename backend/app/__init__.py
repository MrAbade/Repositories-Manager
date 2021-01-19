__version__ = '0.1.0'


from flask import Flask


def create_app(config='production'):
    app = Flask(__name__)

    return app
    