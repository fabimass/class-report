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
        
    def pending_submissions(self):
        return self.pulls.all()[0].quantity
        

class Commit(models.Model):
    name = models.CharField(max_length=99)
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE, related_name="commits")

    def __str__(self):
        return f"{self.repo}/{self.name}"
    
    def is_submitted(self, branch):
        return self.branches.filter(id=branch.id).exists()


class Branch(models.Model):
    name = models.CharField(max_length=99)
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE, related_name="branches")
    commits = models.ManyToManyField(Commit, blank=True, related_name="branches")

    def __str__(self):
        return f"{self.repo}/{self.name}"
    

class Pull(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.CASCADE, related_name="pulls")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.repo}: {self.quantity}"
