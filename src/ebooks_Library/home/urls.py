from django.urls import path
from . import views

urlpatterns = [
   path('signup', views.signup, name='signup'),
   path('signin/', views.signin, name='signin'),
   path('signout/', views.signout, name='signout'),
   path('', views.index, name='home'),
   path('about/', views.about, name='about'),
   path('social_media/', views.social_media, name='social'),
   path('contacts/', views.contacts, name='success_page'),
   path('ebooks/add', views.ebook_add, name='ebook_add'),
   path('ebooks/list', views.ebook_list, name='ebook_list'),
   path('ebooks/edit/<int:pk>/', views.ebookupdate, name='ebookupdate'),
   path('ebooks/delete/<int:pk>/', views.ebookdelete, name='ebookdelete'),
   path('audiobooks/add', views.audiobook_add, name='audiobook_add'),
   path('audiobooks/list', views.audiobook_list, name='audiobook_list'),
   path('audiobooks/edit/<int:pk>/', views.audiobookupdate, name='audiobookupdate'),
]
