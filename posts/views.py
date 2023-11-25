from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.http.response import JsonResponse
from django.http.request import HttpRequest

from posts.models import Post
from posts.serializers import PostSerializer

from comments.models import Comment
from comments.serializers import CommentSerializer

@api_view(['GET', 'POST'])
def post_list(request: HttpRequest):
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
def post_detail(request: HttpRequest, id):
  try:
    post = Post.objects.get(id=id)
    print(post)
    if request.method == 'GET':
      post_serializer = PostSerializer(post)
      return JsonResponse(post_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
      isPartial = bool(request.method == 'PATCH')
      post_data = JSONParser().parse(request)
      
      post_serializer = PostSerializer(post, data=post_data, partial=isPartial)
      if post_serializer.is_valid():
        post_serializer.save();
        return JsonResponse(post_serializer.data, status=status.HTTP_200_OK)
      return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      post.delete()
      return JsonResponse(
        {'message': 'Post was deleted successfully!'},
        status=status.HTTP_204_NO_CONTENT
      )

  except:
    return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def post_comments(request: HttpRequest, id):
  try:
    comment_list = Comment.objects.filter(postId=id)
    comment_serializer = CommentSerializer(comment_list, many=True)
    return JsonResponse(comment_serializer.data, safe=False, status=status.HTTP_200_OK)
  except:
    return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)
