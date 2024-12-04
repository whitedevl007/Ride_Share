# ride/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import viewsets
from .models import Ride
from .serializers import RideSerializer
from rest_framework.views import APIView

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    
class RideStatusUpdateView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'status' in request.data:
            instance.status = request.data['status']
            instance.save()
            return Response({"message": "Ride status updated"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
class RideMatchingView(APIView):
    def post(self, request, *args, **kwargs):
        ride_id = request.data.get('ride_id')
        driver_id = request.data.get('driver_id')
        try:
            ride = Ride.objects.get(id=ride_id)
            ride.driver_id = driver_id
            ride.status = 'started'
            ride.save()
            return Response({"message": "Ride matched with driver"}, status=status.HTTP_200_OK)
        except Ride.DoesNotExist:
            return Response({"message": "Ride not found"}, status=status.HTTP_404_NOT_FOUND)