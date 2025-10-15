

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.contrib import messages

from .models import Booking, Contact, Driver, Review
from .forms import BookingForm, ContactForm, ReviewForm

class IsRiderMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'RIDER'

class IsDriverMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'DRIVER'


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'create_contact.html'
    success_url = reverse_lazy('book-taxi')

    def form_valid(self, form):
        return super().form_valid(form)


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
    

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


def borabora_details_view(request):
    return render(request, 'borabora-details.html')

def shimoni_caves_view(request):
    return render(request, 'shimoni-caves.html')

def kinondo_sacred_forest_view(request):
    return render(request, 'kinondo-sacred.html')

def wasini_dolphin_view(request):
    return render(request, 'wasini-dolphin.html')
  
def shimba_details_view(request):
    """Renders the detailed trip booking page for Masai Mara."""
    return render(request, 'shimba-hills-details.html') 

def diani_retreat_view(request):
    """Renders the detailed trip booking page for Diani Beach Retreat."""
    return render(request, 'diani-retreat-details.html') 


def contact_submit(request):
    """Handle contact form submissions from the site landing page.

    Uses ContactForm to validate input and saves a Contact record. Feedback
    is provided via Django messages and the user is redirected back to home.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks — we've received your message and will be in touch shortly.")
            return redirect('home')
        else:
            # Attach form errors to messages so they can be shown after redirect
            for field, errs in form.errors.items():
                for e in errs:
                    messages.error(request, f"{field}: {e}")
            return redirect('home')
    return redirect('home')
def contact_view(request):
    # 1. Capture the URL parameters from the transfer links
    transfer_dest = request.GET.get('transfer_dest')
    transfer_price = request.GET.get('transfer_price')
    
    # 2. Build the context dictionary
    context = {}
    
    # 3. If transfer details exist, create a pre-filled message
    if transfer_dest and transfer_price:
        context['transfer_message'] = (
            f"Hello, I would like to book a one-way transfer to {transfer_dest}. "
            f"The quoted price is ${transfer_price}. Please confirm availability and next steps."
        )
        context['is_transfer_request'] = True

    return render(request, 'contact.html', context)

def about_view(request):
    """Renders the About Us page."""
    return render(request, 'about.html')
