from django.db import models
from datetime import date

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today < date(today.year, self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"