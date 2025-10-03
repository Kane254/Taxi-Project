from django.contrib import admin
from .models import Booking, Contact, Driver, Vehicle, Review

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'vehicle', 'pickup_location', 'dropoff_location', 'pickup_time', 'booking_time')
    search_fields = ('contact__first_name', 'contact__last_name', 'pickup_location', 'dropoff_location')
    list_filter = ('pickup_time', 'booking_time')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'rating', 'created_at')
    search_fields = ('full_name', 'comment')
    list_filter = ('rating', 'created_at')