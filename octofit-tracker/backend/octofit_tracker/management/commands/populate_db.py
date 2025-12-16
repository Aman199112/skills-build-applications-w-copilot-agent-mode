from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for teams, activities, leaderboard, and workouts
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all data
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            {'email': 'tony@stark.com', 'username': 'IronMan', 'team': 'Marvel'},
            {'email': 'steve@rogers.com', 'username': 'CaptainAmerica', 'team': 'Marvel'},
            {'email': 'bruce@wayne.com', 'username': 'Batman', 'team': 'DC'},
            {'email': 'clark@kent.com', 'username': 'Superman', 'team': 'DC'},
        ]
        for u in users:
            User.objects.create_user(email=u['email'], username=u['username'], password='password')

        # Create activities
        Activity.objects.create(user_email='tony@stark.com', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user_email='steve@rogers.com', team='Marvel', type='Cycling', duration=45)
        Activity.objects.create(user_email='bruce@wayne.com', team='DC', type='Swimming', duration=60)
        Activity.objects.create(user_email='clark@kent.com', team='DC', type='Running', duration=50)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        Workout.objects.create(name='Push Ups', difficulty='Easy')
        Workout.objects.create(name='Pull Ups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
