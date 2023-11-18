from django.urls import path
from .views import post_list, update_post

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('post_update/<int:post_id>/', update_post, name="update_post")
]