from django.db import models
# Create your models here.
class Post(models.Model):
  userId = models.IntegerField()
  title = models.CharField(max_length=255, blank=False, default='')
  body = models.CharField(default='')
