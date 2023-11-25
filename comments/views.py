from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.request import HttpRequest
from django.http.response import JsonResponse

from comments.models import Comment
from comments.serializers import CommentSerializer

@api_view(['GET', 'POST'])
def comment_lists(request: HttpRequest):
  if request.method == 'GET':
    postId = request.GET.get('postId')
    
    if postId:
      comments = Comment.objects.filter(postId=postId)
    else:
      comments = Comment.objects.all()

    comment_serializer = CommentSerializer(comments, many=True)
    return JsonResponse(comment_serializer.data, safe=False, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    comment_data = JSONParser().parse(request)
    comment_serializer = CommentSerializer(data=comment_data)
    if comment_serializer.is_valid():
      comment_serializer.save()
      return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request: HttpRequest, id):
  try:
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
      comment_serializer = CommentSerializer(comment)
      return JsonResponse(comment_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
      comment_data = JSONParser().parse(request)
      comment_serializer = CommentSerializer(comment, data=comment_data)
      if comment_serializer.is_valid():
        comment_serializer.save()
        return JsonResponse(comment_serializer.data, status=status.HTTP_200_OK)
      return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      comment.delete()
      return JsonResponse({'message': 'Comment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

  except:
    return JsonResponse({'message': 'Comment does not exist!'}, status=status.HTTP_404_NOT_FOUND)
