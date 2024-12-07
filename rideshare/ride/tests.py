# ride/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ride

class RideModelTest(TestCase):
    def setUp(self):
        self.rider = User.objects.create_user(username='rider', password='password')
        self.driver = User.objects.create_user(username='driver', password='password')
        self.ride = Ride.objects.create(rider=self.rider, pickup_location='A', dropoff_location='B')

    def test_ride_creation(self):
        self.assertEqual(self.ride.rider, self.rider)
        self.assertEqual(self.ride.pickup_location, 'A')
        self.assertEqual(self.ride.dropoff_location, 'B')

    def test_ride_matching(self):
        response = self.client.post('/api/rides/match_ride/', {'ride_id': self.ride.id, 'driver_id': self.driver.id})
        self.assertEqual(response.status_code, 200)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.driver, self.driver)
        self.assertEqual(self.ride.status, 'started')

    def test_ride_status_update(self):
        response = self.client.patch(f'/api/rides/{self.ride.id}/status/', {'status': 'completed'})
        self.assertEqual(response.status_code, 200)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.status, 'completed')

    def test_real_time_ride_tracking(self):
        self.ride.status = 'started'
        self.ride.save()
        self.assertEqual(self.ride.current_location, "Updated Location")

class RideMatchingTest(TestCase):
    def setUp(self):
        self.rider = User.objects.create_user(username='rider', password='password')
        self.driver = User.objects.create_user(username='driver', password='password')
        self.ride = Ride.objects.create(rider=self.rider, pickup_location='A', dropoff_location='B')

    def test_ride_matching_algorithm(self):
        response = self.client.post('/api/rides/match_ride/', {'ride_id': self.ride.id, 'driver_id': self.driver.id})
        self.assertEqual(response.status_code, 200)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.driver, self.driver)
        self.assertEqual(self.ride.status, 'started')

    def test_ride_status_updates(self):
        response = self.client.patch(f'/api/rides/{self.ride.id}/status/', {'status': 'completed'})
        self.assertEqual(response.status_code, 200)
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.status, 'completed')

    def test_real_time_ride_tracking_simulation(self):
        self.ride.status = 'started'
        self.ride.save()
        self.assertEqual(self.ride.current_location, "Updated Location")
