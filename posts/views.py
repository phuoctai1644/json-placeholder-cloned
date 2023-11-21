from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from posts.models import Post
from posts.serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
  # Get all post
  if request.method == 'GET':
    posts = Post.objects.all()
    post_serializer = PostSerializer(posts, many=True)

    return JsonResponse(post_serializer.data, safe=False)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, id):
  return False
