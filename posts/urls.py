from django.urls import path
from posts import views

urlpatterns = [
    path('', views.post_list),
    path('<int:id>', views.post_detail)
]
