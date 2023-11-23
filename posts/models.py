from django.db import models
# Create your models here.
class Post(models.Model):
  userId = models.ForeignKey('comments.Comment', on_delete=models.CASCADE)
  title = models.CharField(max_length=255, blank=False, default='')
  body = models.CharField(default='')
