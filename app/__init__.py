from ensurepip import bootstrap
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def createapp(config_class=Config):
    """factory function"""

    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init__app(app)

    """registering blueprints"""
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    return app