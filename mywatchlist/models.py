from django.db import models

class MyWatchList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=1)
    release_date = models.TextField()
    review = models.TextField()