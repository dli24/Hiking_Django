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
  
