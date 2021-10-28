from pymongo import MongoClient
from app.read_env import (
    postgres_user,
    postgres_password,
    postgres_host,
    postgres_port,
    postgres_database,
    mongocloud_user,
    mongocloud_password,
    mongocloud_database,
    mongo_host,
    mongo_port,
)
import os

file_path = os.path.abspath(os.getcwd()) + "\database.db"

TESTING = False
DEBUG = True
FLASK_ENV = "development"
FLASK_APP = "app"

SQLALCHEMY_DATABASE_URI = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"

# SQLALCHEMY_DATABASE_URI = (
#   "postgresql://postgres:admin@host.docker.internal/flask-products"
# )
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path

SQLALCHEMY_TRACK_MODIFICATIONS = False


#  mongodb+srv://admin:<password>@cluster0.zf6h5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# connection string for cloud (mongo atlas)
# cluster = f"mongodb+srv://{mongocloud_user}:{mongocloud_password}@cluster0.zf6h5.mongodb.net/{mongocloud_database}?retryWrites=true&w=majority"

# on localhost - mongodb compass, for docker change with service name
db_url = f"mongodb://{mongo_host}:{mongo_port}/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = MongoClient(db_url)
