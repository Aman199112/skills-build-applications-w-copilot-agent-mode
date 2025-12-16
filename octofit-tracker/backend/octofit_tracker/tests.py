from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', team='TestTeam', type='Run', duration=10)
        self.assertEqual(activity.type, 'Run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='TestTeam', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Push Up', difficulty='Easy')
        self.assertEqual(workout.name, 'Push Up')
