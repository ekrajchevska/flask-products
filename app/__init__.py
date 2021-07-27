from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()

def init_app(testing=False):

    """Initialize the core application from a config file in the /instance folder."""
    app = Flask(__name__, instance_relative_config=True)    

    if testing :
        app.config.from_pyfile('config_testing.py')
    else:
        app.config.from_pyfile('config.py')

    # Initialize plugins
    db.init_app(app)
    ma.init_app(app)

    # Register within app context
    with app.app_context():
        from . import routes   
        db.create_all()         

        return app