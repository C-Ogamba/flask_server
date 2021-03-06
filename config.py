import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """General config parent class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'