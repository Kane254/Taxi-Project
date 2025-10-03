

from django.db import models
from users.models import User, Driver

class Vehicle(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField(default=4)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Contact: {self.first_name} {self.last_name}"


class Booking(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='bookings')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_time = models.DateTimeField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.contact} from {self.pickup_location} to {self.dropoff_location}"
    

class Review(models.Model):
    #booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='review')
    full_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review - Rating: {self.rating}"