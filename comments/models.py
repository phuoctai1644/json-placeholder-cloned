from django.db import models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
  postId = models.ForeignKey(Post, on_delete=models.CASCADE)
  name = models.CharField(blank=False, default='')
  email = models.CharField(blank=False, default='')
  body = models.CharField(blank=False, default='')
