from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class CarDetail(generics.RetrieveDestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImage
    
class CarImageList(generics.ListAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class BookingList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
 
