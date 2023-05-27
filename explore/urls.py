from django.contrib import admin
from django.urls import path
from explore import views


urlpatterns = [
    path('', views.explore, name='explore'),
    path('Contact', views.Contact, name='Contact'),
    path('exploreplaces/<str:country>', views.city, name='city'),
    path('exploreplaces/<str:country>/<str:city>', views.explorePlaces, name='exploreplaces'),
   

]   