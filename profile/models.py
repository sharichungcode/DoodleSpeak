from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Activated"),
    (1, "Suspended"),
    (2, "Deactivated"),
)

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.user.username

