from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField


class CustomUser(AbstractUser):
    avatar = ResizedImageField(size=[512, 512], crop=['middle', 'center'], force_format='JPEG', quality=90, blank=True, null=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return self.username

