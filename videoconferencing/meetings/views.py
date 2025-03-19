# meetings/views.py
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect  # For POST requests
from django.views.decorators.clickjacking import xframe_options_exempt  # For iframe embedding
import uuid

def home(request):
    """Render the homepage with options to create or join a meeting."""
    return render(request, 'meetings/home.html')

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



# from rest_framework import status, generics
# from rest_framework.response import Response
# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
# from django.urls import reverse
# import uuid
# from .serializers import MeetingSerializer  # Assuming serializers.py exists

# class HomeView(generics.GenericAPIView):
#     """API endpoint to provide homepage options."""
#     serializer_class = MeetingSerializer

#     def get(self, request, *args, **kwargs):
#         """Return options to create or join a meeting as JSON."""
#         data = {
#             "message": "Welcome to the meetings API. Use /create_meeting/ to create a meeting or /join_meeting/ to join an existing meeting."
#         }
#         return Response(data, status=status.HTTP_200_OK)

# class CreateMeetingView(generics.GenericAPIView, CreateModelMixin):
#     """API endpoint to create a new meeting."""
#     serializer_class = MeetingSerializer

#     def post(self, request, *args, **kwargs):
#         """Generate a unique room name and return it."""
#         room_name = uuid.uuid4().hex
#         redirect_url = reverse('meeting', kwargs={'room_name': room_name})
#         data = {"room_name": room_name, "redirect_url": redirect_url}
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class JoinMeetingView(generics.GenericAPIView):
#     """API endpoint to join an existing meeting."""
#     serializer_class = MeetingSerializer

#     def post(self, request, *args, **kwargs):
#         """Handle the form submission to join an existing meeting."""
#         room_name = request.data.get('room_name')  # Use request.data for DRF
#         if room_name:
#             redirect_url = reverse('meeting', kwargs={'room_name': room_name})
#             return Response({"room_name": room_name, "redirect_url": redirect_url}, status=status.HTTP_200_OK)
#         return Response({"error": "Room name is required."}, status=status.HTTP_400_BAD_REQUEST)

# class MeetingView(generics.GenericAPIView, RetrieveModelMixin):
#     """API endpoint to retrieve meeting details."""
#     serializer_class = MeetingSerializer
#     lookup_field = 'room_name'  # Define how room_name is passed (via URL)

#     def get(self, request, room_name, *args, **kwargs):
#         """Return the meeting information."""
#         data = {"room_name": room_name}
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
import uuid

class HomeView(TemplateView):
    """Render the homepage with options to create or join a meeting."""
    template_name = 'meetings/home.html'

    def get(self, request, *args, **kwargs):
        """Render the home template."""
        return super().get(request, *args, **kwargs)
    
@method_decorator(csrf_exempt, name='dispatch')
class CreateMeetingView(View):
    """Generate a unique room name and redirect to the meeting page."""

    def post(self, request, *args, **kwargs):
        """Handle POST request to create a meeting."""
        room_name = uuid.uuid4().hex
        return redirect('meeting', room_name=room_name)

    def get(self, request, *args, **kwargs):
        """Redirect to home if accessed via GET."""
        # return redirect('home')
        room_name = uuid.uuid4().hex  # Still available for POST if needed
        return redirect('meeting', room_name=room_name)

@method_decorator(csrf_exempt, name='dispatch')
class JoinMeetingView(View):
    """Handle the form submission to join an existing meeting."""

    def post(self, request, *args, **kwargs):
        """Process the form submission and redirect to the meeting."""
        print("POST data:", request.POST)  # Debug: Print the POST data
        room_name = request.POST.get('room_name')
        print("room_name:", room_name)
        if room_name:
            return redirect('meeting', room_name=room_name)
        return redirect('home')

    def get(self, request, *args, **kwargs):
        """Redirect to home if accessed via GET."""
        return redirect('home')

class MeetingView(View):
    """Render the meeting page with the Jitsi Meet interface."""
    template_name = '/Volumes/Murali ext 1/jitsi-django/videoconferencing/meetings/templates/meetings/meeting.html'

    # Exempt from X-Frame-Options to allow embedding Jitsi Meet iframe
    # @method_decorator(lambda x: xframe_options_exempt(x))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # def get(self, request, room_name, *args, **kwargs):
    #     """Render the meeting template with the room_name."""
    #     return render(request, self.template_name, {'room_name': room_name})

    @xframe_options_exempt
    def get(self, request, room_name, *args, **kwargs):
        return render(request, 'meetings/meeting.html', {'room_name': room_name})