from django.urls import path
from .views import post_list, update_post, create_post, delete_post

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('update_post/<int:post_id>/', update_post, name="update_post"),
    path('create_post/', create_post, name="create_post"),
    path('delete_post/<int:post_id>/', delete_post, name="delete_post")
]