from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.http.response import JsonResponse

from posts.models import Post
from posts.serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
  # Get all post
  if request.method == 'GET':
    posts = Post.objects.all()
    post_serializer = PostSerializer(posts, many=True)

    return JsonResponse(post_serializer.data, safe=False, status=status.HTTP_200_OK)
    
  elif request.method == 'POST':
    post_data = JSONParser().parse(request)
    post_serializer = PostSerializer(data=post_data)
    if (post_serializer.is_valid()):
      post_serializer.save()
      return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, id):
  try:
    post = Post.objects.get(id=id)
  except:
    return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)
