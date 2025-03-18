# meetings/views.py
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect  # For POST requests
from django.views.decorators.clickjacking import xframe_options_exempt  # For iframe embedding
import uuid

# def home(request):
#     """Render the homepage with options to create or join a meeting."""
#     return render(request, 'meetings/home.html')

# def create_meeting(request):
#     """Generate a unique room name and redirect to the meeting page."""
#     room_name = uuid.uuid4().hex
#     return redirect('meeting', room_name=room_name)

# @csrf_protect  # Ensure CSRF protection for POST requests
# def join_meeting(request):
#     """Handle the form submission to join an existing meeting."""
#     if request.method == 'POST':
#         room_name = request.POST.get('room_name')
#         if room_name:
#             return redirect('meeting', room_name=room_name)
#     return redirect('home')

# @xframe_options_exempt  # Allow embedding in iframes
# def meeting(request, room_name):
#     """Render the meeting page with the Jitsi Meet interface."""
#     return render(request, 'meetings/meeting.html', {'room_name': room_name})



# meetings/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse
import uuid

class HomeView(APIView):
    """API endpoint to render the homepage options."""
    
    def get(self, request):
        """Return options to create or join a meeting."""
        return Response({"message": "Welcome to the meetings API. Use /create/ to create a meeting or /join/ to join an existing meeting."})

class CreateMeetingView(APIView):
    """API endpoint to create a new meeting."""
    
    def post(self, request):
        """Generate a unique room name and return it."""
        room_name = uuid.uuid4().hex
        return Response({"room_name": room_name}, status=status.HTTP_201_CREATED)

class JoinMeetingView(APIView):
    """API endpoint to join an existing meeting."""
    
    def post(self, request):
        """Handle the form submission to join an existing meeting."""
        room_name = request.data.get('room_name')
        if room_name:
            return Response({"redirect_url": reverse('meeting', kwargs={'room_name': room_name})}, status=status.HTTP_200_OK)
        return Response({"error": "Room name is required."}, status=status.HTTP_400_BAD_REQUEST)

class MeetingView(APIView):
    """API endpoint to render the meeting page."""
    
    def get(self, request, room_name):
        """Return the meeting information."""
        return Response({"room_name": room_name}, status=status.HTTP_200_OK)