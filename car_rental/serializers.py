from rest_framework import serializers
from django.conf import settings
from .models import *
from datetime import datetime


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = [
            "user",
            "rented_car",
            "rating",
            "comment",
            "created_at",
        ]

    def validate_rating(self, value):
        if not 0 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value


class CarSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            "brand",
            "model",
            "year",
            "color",
            "description",
            "car_type",
            "seat_capacity",
            "transmission_type",
            "fuel_tank_capacity",
            "price_per_day",
            "is_available",
            "reviews",
        ]


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    dropoff_time = serializers.TimeField(required=False)
    dropoff_date = serializers.DateField(required=False)
    pickup_date = serializers.DateField(required=False)
    pickup_time = serializers.TimeField(required=False)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            "user",
            "rented_car",
            "pickup_location",
            "dropoff_location",
            "dropoff_date",
            "dropoff_time",
            "pickup_date",
            "pickup_time",
            "created_at",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["dropoff_time"] = instance.dropoff_at.time()
        data["dropoff_date"] = instance.dropoff_at.date()
        data["pickup_date"] = instance.pickup_at.date()
        data["pickup_time"] = instance.pickup_at.time()

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = "__all__"
