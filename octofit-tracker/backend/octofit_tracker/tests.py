from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Test Team')
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', activity='Running', duration=30)
        self.assertEqual(str(activity), 'Test User - Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test User', workout='Push-ups', reps=20)
        self.assertEqual(str(workout), 'Test User - Push-ups')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(leaderboard), 'Test Team: 100 pts')
