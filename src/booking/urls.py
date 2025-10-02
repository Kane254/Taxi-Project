# booking/urls.py

from django.urls import path
from .views import BookingCreateView, RiderBookingListView, DriverBookingListView, tsavo_details_view, mara_details_view, diani_retreat_view

urlpatterns = [
    #path('book/', BookingCreateView.as_view(), name='book-taxi'),
    #path('rider/bookings/', RiderBookingListView.as_view(), name='rider-booking-list'),
    #path('driver/dashboard/', DriverBookingListView.as_view(), name='driver-dashboard'),
   path('tsavo_details', tsavo_details_view, name='tsavo_details'),  # New URL pattern
   path('mara_details.html', mara_details_view, name='mara_details'),
   path('diani_retreat.html', diani_retreat_view, name='diani_retreat'),
]