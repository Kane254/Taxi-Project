

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden

from .models import Booking, Driver
from .forms import BookingForm

class IsRiderMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'RIDER'

class IsDriverMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'DRIVER'

class BookingCreateView(IsRiderMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'
    success_url = reverse_lazy('rider-booking-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Logic to find and assign an available driver
        try:
            driver = Driver.objects.filter(is_available=True).first()
            if driver:
                form.instance.driver = driver
                form.instance.status = 'CONFIRMED'
                driver.is_available = False
                driver.save()
            else:
                form.instance.status = 'PENDING'
        except Driver.DoesNotExist:
            form.instance.status = 'PENDING'
        return super().form_valid(form)

class RiderBookingListView(IsRiderMixin, ListView):
    model = Booking
    template_name = 'rider_booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_time')

class DriverBookingListView(IsDriverMixin, ListView):
    model = Booking
    template_name = 'driver_dashboard.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        try:
            driver_profile = self.request.user.driver
            return Booking.objects.filter(driver=driver_profile).order_by('-pickup_time')
        except Driver.DoesNotExist:
            return Booking.objects.none()

class ptsavo_details(DetailView):
    model = Booking
    template_name = 'tsavo-details.html'
    context_object_name = 'booking'

    def get_object(self):
        # For demonstration, we return a dummy booking object
        return get_object_or_404(Booking, pk=1)  # Replace with actual logic -
    


def tsavo_details_view(request):
    return render(request, 'tsavo-details.html')