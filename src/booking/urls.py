# booking/urls.py

from django.urls import path
from . import views

from .views import BookingCreateView, RiderBookingListView, DriverBookingListView, borabora_details_view, shimba_details_view, diani_retreat_view, shimoni_caves_view, kinondo_sacred_forest_view, congo_sunset_details_view, wasini_dolphin_view, contact_view, contact_submit, ReviewCreateView, about_view


urlpatterns = [
    #path('book/', BookingCreateView.as_view(), name='book-taxi'),
    #path('rider/bookings/', RiderBookingListView.as_view(), name='rider-booking-list'),
    #path('driver/dashboard/', DriverBookingListView.as_view(), name='driver-dashboard'),
    path('borabora_details', borabora_details_view, name='borabora_details'),  # New URL pattern
    path('shimoni_caves', shimoni_caves_view, name='shimoni_caves'),  # New URL pattern
    path('kinondo_sacred', kinondo_sacred_forest_view, name='kinondo_sacred'),  # New URL pattern
    path('wasini_dolphin', wasini_dolphin_view, name='wasini_dolphin'),  # New URL pattern
    path('shimba_details.html', shimba_details_view, name='shimba_details'),
    path('diani_retreat.html', diani_retreat_view, name='diani_retreat'),
    path('congo_sunset_details', congo_sunset_details_view, name='congo_sunset'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('reviews/', ReviewCreateView.as_view(), name='review_new'),
    path('contact.html', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]