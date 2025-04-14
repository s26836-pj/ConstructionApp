from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    position = models.CharField(max_length=100, blank=True, null=True)
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
