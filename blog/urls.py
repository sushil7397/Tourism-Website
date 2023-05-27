from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('', views.blogHome, name='blogHome'),
    path('Contact', views.Contact, name='Contact'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    path('category/<str:category>', views.category, name='category'), 
    
    
]   