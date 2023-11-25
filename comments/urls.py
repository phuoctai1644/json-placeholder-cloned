from django.urls import path
from comments import views

urlpatterns = [
  path('', views.comment_lists),
  path('<int:id>', views.comment_detail)
]
