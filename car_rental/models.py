import os
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


def rename_file(instance, filename):
    extenstion = os.path.splitext(filename)[1]
    car_id = instance.car.id
    # To get the number of images for a car
    images_count = instance.car.images.count()
    if images_count == 0:
        count = 0
    else:
        count = images_count + 1

    new_filename = f"car_{car_id}_{count}{extenstion}"
    return os.path.join("Car_images", f"car_{car_id}", new_filename)


def rename_pfp(instance, filename):
    ext = os.path.splitext(filename)[1]
    user_id = instance.id
    filename = f"user_{user_id}{ext}"
    return os.path.join("Profile_pictures", filename)


class MorentUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to=rename_pfp, blank=True)
    job_title = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    role = models.CharField(
        max_length=10,
        choices=[("admin", "Admin"), ("customer", "Customer")],
        default="customer",
    )

    objects = MorentUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    description = models.TextField()
    car_type = models.CharField(max_length=10, db_index=True)
    seat_capacity = models.IntegerField(db_index=True)
    transmission_type = models.CharField(
        max_length=5, choices=[("MAN", "Manual"), ("AUTO", "Automatic")]
    )
    fuel_tank_capacity = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    is_available = models.BooleanField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image_url = models.ImageField(upload_to=rename_file)

    def __str__(self):
        return f"{self.car.brand} {self.car.model} {self.car.year}"


class CarUserId(models.Model):
    rented_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Booking(CarUserId):
    pickup_location = models.CharField(max_length=20)
    dropoff_location = models.CharField(max_length=20)
    dropoff_at = models.DateTimeField()
    pickup_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        default_related_name = "bookings"

    def __str__(self):
        return f"{self.user.first_name} books {self.rented_car.brand} {self.rented_car.model} {self.rented_car.year}"


class Review(CarUserId):
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = "reviews"

    def __str__(self):
        return f"{self.user.first_name} added a review on {self.rented_car.brand} {self.rented_car.model} {self.rented_car.year}"
