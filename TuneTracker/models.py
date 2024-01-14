from django.db import models

# Create your models here.

# Artist Model
class Artist(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#Song Model
    
class Song(models.Model):
    title = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist ,on_delete=models.CASCADE,null = False)

    def __str__(self):
        return self.title
