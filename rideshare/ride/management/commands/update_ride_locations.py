from django.core.management.base import BaseCommand
from ride.models import Ride
import time

class Command(BaseCommand):
    help = 'Update ride locations periodically'

    def handle(self, *args, **kwargs):
        while True:
            rides = Ride.objects.filter(status='started')
            for ride in rides:
                # Simulate location update
                ride.current_location = "Updated Location"
                ride.save()
            time.sleep(60)  # Update every minute