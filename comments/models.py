from django.db import models

# Create your models here.
class Comment(models.Model):
  postId = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
  name = models.CharField(blank=False, default='')
  email = models.CharField(blank=False, default='')
  body = models.CharField(blank=False, default='')
