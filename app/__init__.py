from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from werkzeug.routing import Rule
from instance.config import client


# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()
doc_db = client.flaskproducts
migrate = Migrate(db)


def init_app(testing=False):

    """Initialize the core application from a config file in the /instance folder."""
    app = Flask(__name__, instance_relative_config=True)

    if testing:
        app.config.from_pyfile("config_testing.py")
    else:
        app.config.from_pyfile("config.py")

    app.url_rule_class = lambda path, **options: Rule("/products-api" + path, **options)

    # Initialize plugins
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Register within app context
    with app.app_context():
        from .routes import products, categories, document

        db.create_all()
        print(f"MongoDbs:  {client.list_database_names()}")
        col = doc_db["products"]
        print(f"Collection: {doc_db.list_collection_names()}")

        return app
