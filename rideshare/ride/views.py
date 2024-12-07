

# # ride/views.py
# from datetime import time
# import threading
# from rest_framework import generics, status
# from rest_framework.response import Response
# from django.contrib.auth import authenticate, login
# from .serializers import UserRegistrationSerializer, UserLoginSerializer
# from rest_framework import viewsets
# from .models import Ride
# from .serializers import RideSerializer
# from rest_framework.views import APIView
# from geopy.distance import geodesic
# from django.contrib.auth.models import User

# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserRegistrationSerializer

# class UserLoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
#         if user:
#             login(request, user)
#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#         return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# class RideViewSet(viewsets.ModelViewSet):
#     queryset = Ride.objects.all()
#     serializer_class = RideSerializer

# class RideStatusUpdateView(generics.UpdateAPIView):
#     queryset = Ride.objects.all()
#     serializer_class = RideSerializer

#     def partial_update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if 'status' in request.data:
#             instance.status = request.data['status']
#             instance.save()
#             return Response({"message": "Ride status updated"}, status=status.HTTP_200_OK)
#         return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

# class RideMatchingView(APIView):
#     def post(self, request, *args, **kwargs):
#         ride_id = request.data.get('ride_id')
#         print(f"Received ride_id: {ride_id}")  # Debugging statement
#         try:
#             ride = Ride.objects.get(id=ride_id)
#             print(f"Found ride: {ride}, Status: {ride.status}")  # Debugging statement
#             if ride.status != 'requested':
#                 return Response({"message": "Ride is not in 'requested' status"}, status=status.HTTP_400_BAD_REQUEST)
#             available_drivers = User.objects.filter(rides_as_driver__isnull=True)
#             print(f"Available drivers: {available_drivers}")  # Debugging statement
#             closest_driver = self.find_closest_driver(ride, available_drivers)
#             if closest_driver:
#                 ride.driver = closest_driver
#                 ride.status = 'started'
#                 ride.save()
#                 threading.Thread(target=self.update_ride_location, args=(ride.id,)).start()  # Start location updates
#                 return Response({"message": "Ride matched with driver"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"message": "No available drivers"}, status=status.HTTP_404_NOT_FOUND)
#         except Ride.DoesNotExist:
#             print(f"Ride with id {ride_id} not found")  # Debugging statement
#             return Response({"message": "Ride not found"}, status=status.HTTP_404_NOT_FOUND)

#     def find_closest_driver(self, ride, drivers):
#         ride_location = (ride.pickup_location_lat, ride.pickup_location_lon)
#         closest_driver = None
#         min_distance = float('inf')
#         for driver in drivers:
#             driver_location = (driver.current_location_lat, driver.current_location_lon)
#             distance = geodesic(ride_location, driver_location).km
#             if distance < min_distance:
#                 min_distance = distance
#                 closest_driver = driver
#         return closest_driver

#     def update_ride_location(self, ride_id):
#         while True:
#             try:
#                 ride = Ride.objects.get(id=ride_id, status='started')
#                 # Simulate location update
#                 ride.current_location = "Updated Location"
#                 ride.save()
#                 time.sleep(60)  # Update every minute
#             except Ride.DoesNotExist:
#                 break









# ride/views.py
from datetime import time
import threading
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import viewsets
from .models import Ride, Driver
from .serializers import RideSerializer
from rest_framework.views import APIView
from geopy.distance import geodesic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

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

        # Get the ride and driver objects
        ride = get_object_or_404(Ride, id=ride_id)
        driver = get_object_or_404(User, id=driver_id)

        # Check if the ride is in 'requested' status
        if ride.status != 'requested':
            return Response({"message": "Ride is not in 'requested' status"}, status=status.HTTP_400_BAD_REQUEST)

        # Update the ride with the driver and change the status to 'started'
        ride.driver = driver
        ride.status = 'started'
        ride.save()

        return Response({"message": "Ride matched with driver"}, status=status.HTTP_200_OK)

    def update_ride_location(self, ride_id):
        while True:
            try:
                ride = Ride.objects.get(id=ride_id, status='started')
                ride.current_location = "Updated Location"  # Replace with actual location update logic
                ride.save()
                time.sleep(60)  # Update every minute
            except Ride.DoesNotExist:
                break