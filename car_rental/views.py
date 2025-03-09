from .serializers import *
from .models import *
from rest_framework import generics
from .permissions import *
from rest_framework.permissions import IsAuthenticated


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [
        IsAdminorReadOnly,
    ]


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [
        IsAdminorReadOnly,
    ]


class CarImageList(generics.ListCreateAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [
        IsAdminorReadOnly,
    ]


class CarImageDetail(generics.RetrieveDestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [
        IsAdminorReadOnly,
    ]


# only manager should be able to review and see all bookings
# user should be able to see all their bookings
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsReviewOwnerorAdmin,
    ]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsReviewOwnerorAdmin,
    ]


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == "admin":
            return Booking.objects.all()
        
        return Booking.objects.filter(user=user)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = []
