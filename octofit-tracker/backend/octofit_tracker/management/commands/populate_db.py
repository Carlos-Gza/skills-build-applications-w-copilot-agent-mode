from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email
        db.users.create_index([("email", 1)], unique=True)

        # Sample data
        marvel_team = {"name": "Team Marvel", "members": ["Iron Man", "Captain America", "Thor", "Black Widow"]}
        dc_team = {"name": "Team DC", "members": ["Superman", "Batman", "Wonder Woman", "Flash"]}
        db.teams.insert_many([marvel_team, dc_team])

        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Team Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Team Marvel"},
            {"name": "Thor", "email": "thor@marvel.com", "team": "Team Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Team Marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "Team DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "Team DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "Team DC"},
            {"name": "Flash", "email": "flash@dc.com", "team": "Team DC"},
        ]
        db.users.insert_many(users)

        activities = [
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Superman", "activity": "Cycling", "duration": 45},
            {"user": "Batman", "activity": "Swimming", "duration": 25},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {"team": "Team Marvel", "points": 120},
            {"team": "Team DC", "points": 110},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"user": "Thor", "workout": "Weightlifting", "reps": 100},
            {"user": "Wonder Woman", "workout": "Yoga", "reps": 50},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
