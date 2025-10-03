# booking/urls.py

from django.urls import path

from .views import BookingCreateView, RiderBookingListView, DriverBookingListView, tsavo_details_view, mara_details_view, diani_retreat_view, shimoni_caves_view, kinondo_sacred_forest_view, wasini_dolphin_view, contact_submit, ReviewCreateView

urlpatterns = [
    #path('book/', BookingCreateView.as_view(), name='book-taxi'),
    #path('rider/bookings/', RiderBookingListView.as_view(), name='rider-booking-list'),
    #path('driver/dashboard/', DriverBookingListView.as_view(), name='driver-dashboard'),
    path('tsavo_details', tsavo_details_view, name='tsavo_details'),  # New URL pattern
    path('shimoni_caves', shimoni_caves_view, name='shimoni_caves'),  # New URL pattern
    path('kinondo_sacred', kinondo_sacred_forest_view, name='kinondo_sacred'),  # New URL pattern
    path('wasini_dolphin', wasini_dolphin_view, name='wasini_dolphin'),  # New URL pattern
    path('mara_details.html', mara_details_view, name='mara_details'),
    path('diani_retreat.html', diani_retreat_view, name='diani_retreat'),
    path('contact/submit/', contact_submit, name='contact_submit'),
    path('reviews/', ReviewCreateView.as_view(), name='review_new'),
]