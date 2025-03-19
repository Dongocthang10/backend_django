from django.db import models

# Create your models here.
class Model(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    overview = models.CharField(max_length=5000, blank=True, null=True)
    release_date = models.CharField(max_length=100, blank=True, null=True)
    popularity = models.CharField(max_length=50, blank=True, null=True)
    vote_average = models.CharField(max_length=200, blank=True, null=True)
    vote_count = models.CharField(max_length=200, blank=True, null=True)