from django.db import models

#table for user to app spotyfai

class User(models.Model):
    #characters of users in spotyfai
    name_user = models.CharField(null = False, max_length = 25)
    account = models.CharField(null = False, max_length = 30)
    telephone = models.CharField(null = True, max_length = 15)
    premiun = models.BooleanField(null = False)
    #return data for defec
    def __str__(self):
        return self.name_user