from flask_restful import Resource
from flask import request
from app import db
from models import Episode, Guest, Appearance
from schemas import EpisodeSchema, GuestSchema, AppearanceSchema

# Resource to get a list of all Episodes
class EpisodeList(Resource):
    def get(self):
        # Query all episodes from the database
        episodes = Episode.query.all()
        # Create a schema instance to serialize multiple Episode objects
        episode_schema = EpisodeSchema(many=True)
        # Return serialized episode data and a success message
        return {"message": "Episodes retrieved successfully", "data": episode_schema.dump(episodes)}, 200

# Resource to get details of a specific Episode, including its appearances
class EpisodeDetail(Resource):
    def get(self, id):
        # Query the episode by its ID
        episode = Episode.query.get(id)
        # Check if the episode exists
        if not episode:
            return {"error": "Episode not found"}, 404
        
        # Create an appearance schema instance to serialize associated appearances
        appearance_schema = AppearanceSchema(many=True)
        
        # Format episode data, including nested appearances
        episode_data = {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": appearance_schema.dump(episode.appearances)
        }
        # Return the formatted data and a success message
        return {"message": "Episode retrieved successfully", "data": episode_data}, 200

# Resource to get a list of all Guests
class GuestList(Resource):
    def get(self):
        # Query all guests from the database
        guests = Guest.query.all()
        # Create a schema instance to serialize multiple Guest objects
        guest_schema = GuestSchema(many=True)
        # Return serialized guest data and a success message
        return {"message": "Guests retrieved successfully", "data": guest_schema.dump(guests)}, 200

# Resource to create a new Appearance
class AppearanceCreate(Resource):
    def post(self):
        # Get JSON data from the request
        data = request.json
        try:
            # Create a new Appearance instance with required fields
            new_appearance = Appearance(
                episode_id=data['episode_id'],  # ID of the associated Episode
                guest_id=data['guest_id'],      # ID of the associated Guest
                rating=data['rating']           # Rating of the appearance
            )
            # Add the new appearance to the database session
            db.session.add(new_appearance)
            # Commit the transaction to save the appearance
            db.session.commit()
        
        # Handle case where the data has invalid types
        except ValueError as e:
            return {"errors": [str(e)]}, 400
        
        # Handle missing required fields in the data
        except KeyError:
            return {"errors": ["Invalid input: 'episode_id', 'guest_id', and 'rating' are required fields"]}, 400

        # Create a schema instance to serialize the newly created Appearance
        appearance_schema = AppearanceSchema()
        # Return serialized data of the new appearance and a success message
        return {"message": "Appearance created successfully", "data": appearance_schema.dump(new_appearance)}, 201
