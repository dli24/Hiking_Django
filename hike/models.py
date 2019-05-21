from django.db import models
from accounts.models import Profile

# Create your models here.

class Comments(models.Model):
  hike = models.ForeignKey(
    Hike, on_delete=models.CASCADE, related_name='hike'
  )
  profile = models.ForeignKey(
    Profile, on_delete=models.CASCADE, related_name='profile'
  )
  body = models.CharField(max_length=250)
  rating = models.FloatField()

class Hike(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    distance = models.FloatField()
    difficulty = models.FloatField()
    picture = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.title

class HikeGroup(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE, related_name='hike')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.profile
