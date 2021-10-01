from pymongo import MongoClient
import os

file_path = os.path.abspath(os.getcwd()) + "\database.db"

TESTING = False
DEBUG = True
FLASK_ENV = "development"
FLASK_APP = "app"
SQLALCHEMY_DATABASE_URI = (
    "postgresql://postgres:admin@0.0.0.0:5432/flask_products"  # flask_products
)
# SQLALCHEMY_DATABASE_URI = (
#    "postgresql://postgres:admin@host.docker.internal/flask-products"
# )
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path
SQLALCHEMY_TRACK_MODIFICATIONS = False


#  mongodb+srv://admin:<password>@cluster0.zf6h5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# connection string for cloud (mongo atlas)
# cluster = "mongodb+srv://admin:admin@cluster0.zf6h5.mongodb.net/flaskproducts?retryWrites=true&w=majority"

# on localhost - mongodb compass, for docker change with service name
cluster = "mongodb://0.0.0.0:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = MongoClient(cluster)
