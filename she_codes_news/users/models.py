from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # this is where I would put custom fields - i.e. image, name, etc
    pass

    def __str__(self):
        return self.username