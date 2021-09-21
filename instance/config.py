import os


TESTING = False
DEBUG = True
FLASK_ENV = "development"
FLASK_APP = "app"
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@0.0.0.0:5432/flask_products"
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@host.docker.internal/flask-products'
# SQLALCHEMY_DATABASE_URI = 'sqlite:////database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
