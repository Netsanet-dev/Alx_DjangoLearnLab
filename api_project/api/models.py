from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    club_name = models.CharField(max_length=50)
    age = models.IntegerField()
    player_position = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'