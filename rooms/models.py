from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Room(models.Model):
    
    def __str__(self):
        return "Room %s" % self.id

class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return "'{}' suggests '{}' in room '{}'".format(self.user.name, self.movie.title, self.room.id)