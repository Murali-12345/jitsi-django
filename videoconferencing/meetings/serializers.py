from rest_framework import serializers
from .models import MeetingRoom

# class MeetingRoomSerializer(serializers.Serializer):
#     room_name = serializers.CharField(max_length=100)
#     domain = serializers.CharField(max_length=100, default="meet.jit.si")





# serializers.py
from rest_framework import serializers

class MeetingSerializer(serializers.Serializer):
    room_name = serializers.CharField(max_length=255, required=False)
    redirect_url = serializers.CharField(max_length=255, required=False, allow_blank=True)
    message = serializers.CharField(max_length=255, required=False, allow_blank=True)
    error = serializers.CharField(max_length=255, required=False, allow_blank=True)

  