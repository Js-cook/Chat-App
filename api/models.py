from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
  date = models.DateField()
  time = models.TimeField()
  text = models.CharField(max_length=900)
  sender = models.CharField(max_length=50, default="Anon")

  def __str__(self):
    return self.text
  