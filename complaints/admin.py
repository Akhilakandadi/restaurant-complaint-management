from django.contrib import admin
from django.utils.html import mark_safe  # For rendering HTML in the admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'submitted_at', 'user', 'priority', 'image', 'is_urgent']  # Add image_thumb to list display
    search_fields = ['title', 'description', 'category', 'status']  # Allow searching by title, description, etc.
    list_filter = ['status', 'category', 'priority']  # Filter by status, category, and priority
    ordering = ['-submitted_at']  # Order complaints by submission date (newest first)

admin.site.register(Complaint, ComplaintAdmin)  # Register the model and its custom admin class
