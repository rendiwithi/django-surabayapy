from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('telegram/', views.telegram),
    path('youtube/', views.youtube),
    path('instagram/', views.instagram),
    path('discord/', views.discord),
    path('twitter/', views.twitter),
    path('test/', views.test),
    path('event-detail/<int:idevent>/', views.eventdetail)
]