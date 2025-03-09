from django.urls import path
from .views import *

urlpatterns = [
    path("", CarList.as_view(), name="cars"),
    path("<int:pk>/", CarDetail.as_view(), name="car"),
    path("reviews/", ReviewList.as_view(), name="reviews"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review"),
    path("bookings/", BookingList.as_view(), name="bookings"),
    path("bookings/<int:pk>/", BookingDetail.as_view(), name="booking"),
    path("car-images/", CarImageList.as_view(), name="images"),
    path("car-images/<int:pk>/", CarImageDetail.as_view(), name="image"),
    path("redoc/", redoc_view, name="redoc"),
]
