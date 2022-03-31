from django.db import models

# Create your models here.
class Message(models.Model):
  date = models.DateField()
  time = models.TimeField()
  text = models.CharField(max_length=900)

  def __str__(self):
    return self.text
  