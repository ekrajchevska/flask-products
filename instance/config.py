import os

# os.environ -> dict so envs koi kje se load 
# da vidam kako so dotenv 

TESTING = False
DEBUG = True
FLASK_ENV = 'development'
FLASK_APP = 'app'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@postgres/flask-products'
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@host.docker.internal/flask-products'
SQLALCHEMY_TRACK_MODIFICATIONS = False
