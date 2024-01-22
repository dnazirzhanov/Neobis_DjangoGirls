from django.urls import path
from .views import post_list, add_post, update_post, delete_post, read_more

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('add/', add_post, name='add_post'),
    path('update/<int:pk>/', update_post, name='update_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('read-more/<int:pk>/', read_more, name='read_more'),
]