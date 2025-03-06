from django.urls import path
from .views import *

urlpatterns = [
    path("", CarList.as_view(), name="cars"),
    path("reviews/", ReviewList.as_view(), name="reviews"),
    path("bookings/", BookingList.as_view(), name="booking"),
]