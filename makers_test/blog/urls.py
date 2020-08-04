from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts-list'),
    path('<int:pk>/', post_details, name='post-details'),
    path('add/', add_post, name='add-post'),
    path('update/<int:pk>/', update_post, name='update-post'),
    path('delete/<int:pk>/', delete_post, name='delete-post'),
]