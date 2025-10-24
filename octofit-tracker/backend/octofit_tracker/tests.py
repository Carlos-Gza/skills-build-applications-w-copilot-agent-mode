from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test", email="test@example.com", team="Team Marvel")
        self.assertEqual(user.name, "Test")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team Marvel", members=["Iron Man", "Thor"])
        self.assertEqual(team.name, "Team Marvel")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Test", activity="Running", duration=30)
        self.assertEqual(activity.activity, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team="Team Marvel", points=100)
        self.assertEqual(lb.team, "Team Marvel")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user="Test", workout="Yoga", reps=50)
        self.assertEqual(workout.workout, "Yoga")
