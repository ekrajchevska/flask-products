from pymongo import MongoClient
import os

file_path = os.path.abspath(os.getcwd()) + "\database.db"

TESTING = False
DEBUG = True
FLASK_ENV = "development"
FLASK_APP = "app"

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_port = os.getenv("POSTGRES_PORT")
postgres_database = os.getenv("POSTGRES_DATABASE")
SQLALCHEMY_DATABASE_URI = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"

# SQLALCHEMY_DATABASE_URI = (
#   "postgresql://postgres:admin@host.docker.internal/flask-products"
# )
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path
SQLALCHEMY_TRACK_MODIFICATIONS = False


#  mongodb+srv://admin:<password>@cluster0.zf6h5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# connection string for cloud (mongo atlas)
mongocloud_user = os.getenv("MONGOCLOUD_USER")
mongocloud_password = os.getenv("MONGOCLOUD_PASSWORD")
mongocloud_database = os.getenv("MONGOCLOUD_DATABASE")
# cluster = f"mongodb+srv://{mongocloud_user}:{mongocloud_password}@cluster0.zf6h5.mongodb.net/{mongocloud_database}?retryWrites=true&w=majority"

# on localhost - mongodb compass, for docker change with service name
mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")
db_url = f"mongodb://{mongo_host}:{mongo_port}/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = MongoClient(db_url)
