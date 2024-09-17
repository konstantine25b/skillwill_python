# car_animal_app/models.py
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Animal(models.Model):
    species = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    is_domesticated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.species})"
