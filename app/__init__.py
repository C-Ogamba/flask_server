from flask import Flask
from config import Config

def createapp(config_class=Config):
    """factory function"""

    app = Flask(__name__)
    app.config.from_object(config_class)

    """registering blueprints"""

    return app