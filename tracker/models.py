from django.utils import timezone
from django.db import models

# Create your models here.
class Tracker(models.Model):
    desc = models.TextField()
    amount = models.IntegerField()
    date = models.DateField()
    category = models.CharField(max_length=255)