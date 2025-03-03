from rest_framework import serializers
from django.conf import settings
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        models = Car
        fields = "__all__"
        
        
class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = CarImage
        fields = "__all__"
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        models = Booking
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        models = Review
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = settings.AUTTH_USER_MODEL
        fields = "__all__"