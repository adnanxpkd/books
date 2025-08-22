from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('about/', views.about),
   path('social_media/', views.social_media),
   path('contacts/', views.contacts),
]
