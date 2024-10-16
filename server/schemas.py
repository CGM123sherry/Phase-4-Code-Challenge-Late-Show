from app import ma
from models import Guest, Episode, Appearance

# Guest Schema
class GuestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Guest
        fields = ('id', 'name', 'occupation')

# Episode Schema
class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode
        fields = ('id', 'date', 'number')

# Appearance Schema (Nested guest and episode)
class AppearanceSchema(ma.SQLAlchemyAutoSchema):
    guest = ma.Nested(GuestSchema)
    episode = ma.Nested(EpisodeSchema)

    class Meta:
        model = Appearance
        fields = ('id', 'rating', 'episode_id', 'guest_id', 'guest', 'episode')
