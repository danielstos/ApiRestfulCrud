from flask import Flask
from flask_migrate import Migrate   
from .model import configure as config_db
from .serealizer import configure as config_ma

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/crud'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)
    
    Migrate(app, app.db) 

    from .movies import bp_movies
    app.register_blueprint(bp_movies)
    
    return app