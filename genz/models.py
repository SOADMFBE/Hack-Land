from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('dev','разработчик'),
    ('des','дизайнер'),
    ('manager','менеджер'),
)

CHOICES_track = (
    ('1','трек 1'),
    ('2','трек 2'),
    ('3','трек 3'),
)



class userC_profile(models.Model):
    teamID = models.IntegerField()
    role = models.CharField(choices=CHOICES, max_length=20, default='dev')
    usersData = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)


class teams(models.Model):
    name = models.CharField(max_length=100)
    projectID = models.IntegerField()
    cp1 = models.BooleanField(default=None)
    com1 = models.TextField(max_length=300, default='', blank=True)
    cp2 = models.BooleanField(default=None)
    com2 = models.TextField(max_length=300, default='', blank=True)



class projects(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=2000)
    track = models.TextField(max_length=50, choices=CHOICES_track)

    def __str__(self):
        return self.name

