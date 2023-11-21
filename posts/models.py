from django.db import models

# Create your models here.
class Post(models.Model):
  userId = models.IntegerField()
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255, blank=False, default='')
  body = models.CharField(default='')
