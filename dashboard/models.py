from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    words_history = models.JSONField(blank=True, default=list)

    def __str__(self):
        return f"{self.user.username}'s Dashboard"