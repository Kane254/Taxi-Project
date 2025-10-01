# booking/urls.py

from django.urls import path
from .views import BookingCreateView, RiderBookingListView, DriverBookingListView

urlpatterns = [
    path('book/', BookingCreateView.as_view(), name='book-taxi'),
    path('rider/bookings/', RiderBookingListView.as_view(), name='rider-booking-list'),
    path('driver/dashboard/', DriverBookingListView.as_view(), name='driver-dashboard'),
]