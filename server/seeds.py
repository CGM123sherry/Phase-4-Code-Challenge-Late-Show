import os
import csv
from app import create_app, db  # Change: Import create_app and db
from models import Episode, Guest, Appearance

app = create_app()  # Change: Create an instance of the app

# Ensure your tables are created before seeding
with app.app_context():  # Change: Use the app context
    db.create_all()  # Create tables

    # Change: Generating seed data
    # Example seed data (you can customize this)
    episodes = [
        {"date": "2023-01-01", "number": 1},
        {"date": "2023-01-08", "number": 2},
        {"date": "2023-01-15", "number": 3},
    ]

    guests = [
        {"name": "John Doe", "occupation": "Actor"},
        {"name": "Jane Smith", "occupation": "Comedian"},
        {"name": "Tom Johnson", "occupation": "Musician"},
    ]

    # Add episodes to the database
    for episode in episodes:
        new_episode = Episode(date=episode["date"], number=episode["number"])
        db.session.add(new_episode)

    # Add guests to the database
    for guest in guests:
        new_guest = Guest(name=guest["name"], occupation=guest["occupation"])
        db.session.add(new_guest)

    db.session.commit()  # Commit the session to save changes

    print("Seed data created successfully!")
