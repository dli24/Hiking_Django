from django.db import models
from accounts.models import Profile

# Create your models here.
class Hike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hike')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    hike_date = models.DateField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)
    distance = models.FloatField(null=True)
    difficulty = models.FloatField(null=True)
    created_date = models.DateField(null=True)
    picture = models.TextField(null=True)

    def __str__(self):
        return self.title

        
class Comments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment')
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE, related_name='comment')
    body = models.CharField(max_length=250)
    rating = models.FloatField()

    def __str__(self):
        return self.body

class HikeGroup(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE, related_name='hike_group')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hike_group')

    def __str__(self):
        return self.hike.title

