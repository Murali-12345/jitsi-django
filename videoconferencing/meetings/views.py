# meetings/views.py
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect  # For POST requests
from django.views.decorators.clickjacking import xframe_options_exempt  # For iframe embedding
import uuid

def home(request):
    """Render the homepage with options to create or join a meeting."""
    return render(request, 'meetings/home.html')

def create_meeting(request):
    """Generate a unique room name and redirect to the meeting page."""
    room_name = uuid.uuid4().hex
    return redirect('meeting', room_name=room_name)

@csrf_protect  # Ensure CSRF protection for POST requests
def join_meeting(request):
    """Handle the form submission to join an existing meeting."""
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            return redirect('meeting', room_name=room_name)
    return redirect('home')

@xframe_options_exempt  # Allow embedding in iframes
def meeting(request, room_name):
    """Render the meeting page with the Jitsi Meet interface."""
    return render(request, 'meetings/meeting.html', {'room_name': room_name})