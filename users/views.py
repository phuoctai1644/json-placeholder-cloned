from django.http.request import HttpRequest
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

from users.models import User
from users.serializer import UserSerializer

@api_view(['GET', 'POST'])
def user_lists(request: HttpRequest):
  if request.method == 'GET':
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)

    if user_serializer.is_valid():
      user_serializer.save()
      return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request: HttpRequest, id):
  try:
    user = User.objects.get(id=id)
    if request.method == 'GET':
      user_serializer = UserSerializer(user)
      return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
      user_data = JSONParser().parse(request)
      user_serializer = UserSerializer(user, data=user_data)
      if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
      user.delete()
      return JsonResponse(
        {'message': 'User was deleted successfully!'},
        status=status.HTTP_204_NO_CONTENT
      )
  except:
    return JsonResponse({'message': 'The user does not exit'}, status=status.HTTP_404_NOT_FOUND)
