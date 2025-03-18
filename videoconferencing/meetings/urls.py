# meetings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_meeting/', views.CreateMeetingView.as_view(), name='create_meeting'),
    path('join_meeting/', views.JoinMeetingView.as_view(), name='join_meeting'),
    path('meeting/<str:room_name>/', views.MeetingView.as_view(), name='meeting'),
]