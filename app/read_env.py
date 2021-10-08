import os


# Postgres database
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_port = os.getenv("POSTGRES_PORT")
postgres_database = os.getenv("POSTGRES_DATABASE_FLASK")

# Mongo cloud
mongocloud_user = os.getenv("MONGOCLOUD_USER")
mongocloud_password = os.getenv("MONGOCLOUD_PASSWORD")
mongocloud_database = os.getenv("MONGOCLOUD_DATABASE")

# Mongo locally
mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")


# Auth
SECRET_KEY = os.getenv("secret")
ALGORITHM = os.getenv("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("expire")
