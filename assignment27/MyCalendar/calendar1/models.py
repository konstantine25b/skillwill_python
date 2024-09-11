from django.db import models

class Calendar1(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
