from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('posts_create/', views.posts_create, name='posts_create'),
    path('<int:post_pk>/', views.posts_detail, name='posts_detail'),
    path('<int:post_pk>/posts_delete/', views.posts_delete, name='posts_delete'),
    path('<int:post_pk>/posts_update/', views.posts_update, name='posts_update'),


]