from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(("email address"), blank=True, unique=True)

    def __str__(self):
        return self.email
