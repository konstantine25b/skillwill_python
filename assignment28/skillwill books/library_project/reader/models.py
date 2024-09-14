from django.contrib.auth.models import User
from django.db import models

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username