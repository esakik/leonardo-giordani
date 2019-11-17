from flask import Flask

from flask_settings import DevConfig
from src.rest import room


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(room.blueprint)
    return app
