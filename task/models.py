from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_user = models.ForeignKey(User)
