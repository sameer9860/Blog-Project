from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list_create, name='blog_list'),
    path("", views.my_blogs, name='my_blogs'),
    path('create/', views.blog_create, name='blog_create'),
    path('edit/<slug:slug>/', views.blog_edit, name='blog_edit'),
    path('delete/<slug:slug>/', views.blog_delete, name='blog_delete'),
]
