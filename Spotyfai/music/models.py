from django.db import models

class Artist(models.Model):
    name_artist = models.CharField(null = False, max_length = 30)
    genero = models.CharField(null = False, max_length = 30)
    

    def __str__(self):
        return self.name_artist

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    name_song = models.CharField(null = False, max_length = 30)
    letter = models.TextField(null = True)
    copyright_song = models.BooleanField(null = False)

    def __str__(self):
        return self.name_song 