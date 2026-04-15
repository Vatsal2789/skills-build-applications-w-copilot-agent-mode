from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {'name': 'Marvel'},
            {'name': 'DC'}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Spider-Man', 'email': 'spidey@marvel.com', 'team': 'Marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', 1)], unique=True)

        # Activities
        activities = [
            {'user': 'Iron Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Batman', 'activity': 'Cycling', 'duration': 45},
            {'user': 'Wonder Woman', 'activity': 'Swimming', 'duration': 60},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'user': 'Spider-Man', 'workout': 'Push-ups', 'reps': 50},
            {'user': 'Superman', 'workout': 'Squats', 'reps': 100},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'team': 'Marvel', 'points': 300},
            {'team': 'DC', 'points': 250},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
