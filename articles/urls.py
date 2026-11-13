from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('articles/', views.liste_articles, name='articles'),
    path('articles/<int:id>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('home/', views.accueil, name='home'),
]
