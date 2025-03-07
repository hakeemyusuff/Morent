from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarImageList(generics.ListCreateAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    
class CarImageDetail(generics.RetrieveDestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
 
#only manager should be able to review and see all bookings
#user should be able to see all bookings   
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
