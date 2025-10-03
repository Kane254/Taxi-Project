# booking/forms.py

from django import forms
from .models import Booking, Contact, Review

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_location', 'dropoff_location', 'pickup_time']
        widgets = {
            'pickup_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['full_name', 'rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }