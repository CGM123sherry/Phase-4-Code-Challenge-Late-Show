from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api


# Initialize extensions globally
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

# Configuration class
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # or your actual database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Change: Create a factory function to initialize the app and extensions
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Initialize the API and add resources
    api = Api(app)  # Initialize API
    
    from resources import EpisodeList, EpisodeDetail, GuestList, AppearanceCreate  # Import resources
    # Registering routes
    api.add_resource(EpisodeList, '/episodes')  
    api.add_resource(EpisodeDetail, '/episodes/<int:id>')
    api.add_resource(GuestList, '/guests')
    api.add_resource(AppearanceCreate, '/appearances')
   

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

