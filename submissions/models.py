from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    pass


class Sync(models.Model):
    last_sync = models.DateTimeField()


class Repo(models.Model):
    name = models.CharField(max_length=99)
    owner = models.CharField(max_length=99)
    private = models.BooleanField()
    token = models.CharField(blank=True,max_length=256)

    def __str__(self):
        return f"{self.owner}/{self.name}"
    
    def clean(self):
        if self.private == True and self.token is '':
            raise ValidationError('Token is required for private repos')