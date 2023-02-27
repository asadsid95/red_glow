from flask import Flask

import os

# from .login import login_a
from . import login

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'movies.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app