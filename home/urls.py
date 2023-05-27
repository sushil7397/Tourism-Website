from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Contact', views.Contact, name='Contact'),
    path('about', views.about, name='about'),
    path('page3', views.page3, name='page'),
    path('error', views.error_404_view, name='error')
     
]