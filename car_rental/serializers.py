from rest_framework import serializers
from django.conf import settings
from .models import *
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer


User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
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


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["id", "image_url"]


class CarSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            "id",
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
            "images",
        ]

    # To limit the reviews to just three in the car serializer
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["reviews"] = data["reviews"][:3]
        return data


class BookingSerializer(serializers.ModelSerializer):
    dropoff_time = serializers.TimeField(required=False)
    dropoff_date = serializers.DateField(required=False)
    pickup_date = serializers.DateField(required=False)
    pickup_time = serializers.TimeField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    total_amount = serializers.FloatField(read_only=True)

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
            "total_amount",
            "created_at",
        ]

    # To split the dropoff_at and pickup_at into date and time before displaying
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["dropoff_time"] = instance.dropoff_at.time()
        data["dropoff_date"] = instance.dropoff_at.date()
        data["pickup_date"] = instance.pickup_at.date()
        data["pickup_time"] = instance.pickup_at.time()
        data["total_amount"] = (
            instance.rented_car.price_per_day
            * (data["dropoff_date"] - data["pickup_date"]).days
        )

        return data

    def set_datetime_field(self, data):
        dropoff_date = data.pop("dropoff_date", None)
        dropoff_time = data.pop("dropoff_time", None)
        pickup_time = data.pop("pickup_time", None)
        pickup_date = data.pop("pickup_date", None)

        if dropoff_date and dropoff_time:
            data["dropoff_at"] = timezone.make_aware(
                datetime.combine(dropoff_date, dropoff_time)
            )
        if pickup_date and pickup_time:
            data["pickup_at"] = timezone.make_aware(
                datetime.combine(pickup_date, pickup_time)
            )

        return data

    def create(self, validated_data):
        validated_data = self.set_datetime_field(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.set_datetime_field(validated_data)
        return super().update(instance, validated_data)


class MorentUserCreateSerializer(UserCreateSerializer):
    re_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate(self, attrs):
        password = attrs["password"]
        re_password = attrs["re_password"]
        
        if not password == re_password:
            return serializers.ValidationError("Password do not match.")
        
        return attrs
        
        
    def create(self, validated_data):
        validated_data.pop("re_password")
        return super().create(validated_data)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "re_password",
            "profile_pic",
            "job_title",
            "company",
        )


class MorentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "profile_pic",
            "job_title",
            "company",
        )
