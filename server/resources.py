from flask_restful import Resource
from flask import request
from app import db
from models import Episode, Guest, Appearance
from schemas import EpisodeSchema, GuestSchema, AppearanceSchema

class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        episode_schema = EpisodeSchema(many=True)
        return {"message": "Episodes retrieved successfully", "data": episode_schema.dump(episodes)}, 200

class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        appearance_schema = AppearanceSchema(many=True)
        episode_data = {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": appearance_schema.dump(episode.appearances)
        }
        return {"message": "Episode retrieved successfully", "data": episode_data}, 200

class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        guest_schema = GuestSchema(many=True)
        return {"message": "Guests retrieved successfully", "data": guest_schema.dump(guests)}, 200

class AppearanceCreate(Resource):
    def post(self):
        data = request.json
        try:
            new_appearance = Appearance(
                episode_id=data['episode_id'],
                guest_id=data['guest_id'],
                rating=data['rating']
            )
            db.session.add(new_appearance)
            db.session.commit()
        except ValueError as e:
            return {"errors": [str(e)]}, 400
        except KeyError:
            return {"errors": ["Invalid input: 'episode_id', 'guest_id', and 'rating' are required fields"]}, 400

        appearance_schema = AppearanceSchema()
        return {"message": "Appearance created successfully", "data": appearance_schema.dump(new_appearance)}, 201
