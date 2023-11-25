from django.urls import path
from users import views

urlpatterns = [
  path('', views.user_lists),
  path('<int:id>', views.user_detail)
]
