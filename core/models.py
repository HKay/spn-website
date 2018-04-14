from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Team(models.Model):
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)


class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=now, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)


class SnakeVersion(models.Model):
    class Meta:
        get_latest_by = "created"

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(default=now, blank=True)
    code = models.TextField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    version = models.IntegerField()
    prev_version = models.IntegerField(blank=True, null=True)


class ActiveSnake(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    version = models.ForeignKey(SnakeVersion, on_delete=models.CASCADE)


class SnakeGame(models.Model):
    snake_version = models.ForeignKey(SnakeVersion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField()

    def __str__(self):
        return self.user.username + " " + str(self.start_date)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)

