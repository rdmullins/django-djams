from django.db import models

# Create your models here.
class Playlist(models.Model):
    title = models.CharField(max_length=100)

class Genre(models.Model):
    genre = models.CharField(max_length=100)

