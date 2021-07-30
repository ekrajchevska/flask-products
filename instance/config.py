import os

# os.environ -> dict so envs koi kje se load 
# da vidam kako so dotenv 

TESTING = False
DEBUG = True
FLASK_ENV = 'development'
FLASK_APP = 'app'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/flask-products'
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@host.docker.internal/flask-test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
