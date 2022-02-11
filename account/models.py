from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    person = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
