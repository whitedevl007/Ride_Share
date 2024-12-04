# ride/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ride

class RideModelTest(TestCase):
    def setUp(self):
        self.rider = User.objects.create_user(username='rider', password='password')
        self.driver = User.objects.create_user(username='driver', password='password')
        self.ride = Ride.objects.create(rider=self.rider, driver=self.driver, pickup_location='A', dropoff_location='B')

    def test_ride_creation(self):
        self.assertEqual(self.ride.rider, self.rider)
        self.assertEqual(self.ride.driver, self.driver)
        self.assertEqual(self.ride.pickup_location, 'A')
        self.assertEqual(self.ride.dropoff_location, 'B')
