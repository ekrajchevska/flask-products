import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()

def init_app(testing=False):

    """Initialize the core application from a config file in the /instance folder."""
    app = Flask(__name__, instance_relative_config=True)    # moze i samo so file (bez instance folderov)

    if testing :
        app.config.from_pyfile('config_testing.py')
    else:
        app.config.from_pyfile('config.py')

    # Initialize plugins
    db.init_app(app)
    ma.init_app(app)

    # Register within app context
    with app.app_context():
        from . import routes    # da probam sto kje se sluci na nova baza ako go nemam ovoj import (probably nema da gi fati site modeli)
        db.create_all()         # ako prethodnovo e true, probaj eden po eden modelive da gi importnesh (from models..)


        return app