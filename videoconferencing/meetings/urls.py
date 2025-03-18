# meetings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_meeting/', views.create_meeting, name='create_meeting'),
    path('join_meeting/', views.join_meeting, name='join_meeting'),
    path('meeting/<str:room_name>/', views.meeting, name='meeting'),
]