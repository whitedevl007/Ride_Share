# # ride/models.py
# from django.db import models
# from django.contrib.auth.models import User

# # class Ride(models.Model):
# #     STATUS_CHOICES = [
# #         ('requested', 'Requested'),
# #         ('started', 'Started'),
# #         ('completed', 'Completed'),
# #         ('cancelled', 'Cancelled'),
# #     ]

# #     rider = models.ForeignKey(User, related_name='rides_as_rider', on_delete=models.CASCADE)
# #     driver = models.ForeignKey(User, related_name='rides_as_driver', on_delete=models.CASCADE, null=True, blank=True)
# #     pickup_location = models.CharField(max_length=255)
# #     dropoff_location = models.CharField(max_length=255)
# #     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)



# class Ride(models.Model):
#     STATUS_CHOICES = [
#         ('requested', 'Requested'),
#         ('started', 'Started'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]

#     rider = models.ForeignKey(User, related_name='rides_as_rider', on_delete=models.CASCADE)
#     driver = models.ForeignKey(User, related_name='rides_as_driver', on_delete=models.CASCADE, null=True, blank=True)
#     pickup_location = models.CharField(max_length=255)
#     dropoff_location = models.CharField(max_length=255)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     current_location = models.CharField(max_length=255, null=True, blank=True)








from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)  # Flag for driver availability


class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    rider = models.ForeignKey(User, related_name='rides_as_rider', on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name='rides_assigned', on_delete=models.CASCADE, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Ride {self.id} from {self.pickup_location} to {self.dropoff_location}"