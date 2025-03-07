from django import forms
from .models import Complaint
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'email', 'category', 'priority', 'image', 'is_urgent']

    # Minimum length for title
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Title must be at least 5 characters long.')
        return title

    # Minimum length for description
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError('Description must be at least 10 characters long.')
        return description

    # Email is mandatory for all complaints
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Email is required for all complaints.')
        return email

    # Optional image file size validation
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError('Image file size must be less than 2MB.')
        return image

    # Cross-field validation: Urgent complaints must have High priority
    def clean(self):
        cleaned_data = super().clean()

        is_urgent = cleaned_data.get('is_urgent')
        priority = cleaned_data.get('priority')

        if is_urgent and priority != 'HI':
            self.add_error('priority', 'Urgent complaints must have High priority.')

        return cleaned_data
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
