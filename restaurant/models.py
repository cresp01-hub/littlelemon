from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
