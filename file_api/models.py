from django.db import models

# Create your models here.

class User_data(models.Model):
  image = models.FileField(blank=False, null=False)
  name = models.CharField(max_length=60)
  description = models.CharField(max_length=600)

  def __str__(self):
      return self.name