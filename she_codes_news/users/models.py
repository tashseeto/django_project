from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # this is where I would put custom fields - i.e. image, name, etc
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    

    def __str__(self):
        return self.username