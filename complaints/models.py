from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    # Category Choices
    FOOD = 'FO'
    SERVICE = 'SV'
    CLEANLINESS = 'CL'
    CATEGORY_CHOICES = [
        (FOOD, 'Food'),
        (SERVICE, 'Service'),
        (CLEANLINESS, 'Cleanliness'),
    ]
    
    # Status Choices
    PENDING = 'PE'
    RESOLVED = 'RE'
    IN_PROGRESS = 'IP'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (RESOLVED, 'Resolved'),
        (IN_PROGRESS, 'In Progress'),
    ]
    
    # Priority Choices
    HIGH = 'HI'
    MEDIUM = 'ME'
    LOW = 'LO'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link complaint to user
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    email = models.EmailField(blank=True, null=True)  # Optional email field
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)  # Complaint status
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically set when complaint is submitted
    status_updated_at = models.DateTimeField(auto_now=True)  # Automatically set when status is updated
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=MEDIUM)  # Complaint priority
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)  # Optional image upload field
    #ip_address = models.GenericIPAddressField(blank=True, null=True)  # IP address of the user submitting the complaint
   # location = models.CharField(max_length=255, blank=True, null=True)  # Location of the complaint (optional)
    #resolution = models.TextField(blank=True, null=True)  # Text for the resolution#
    resolved_at = models.DateTimeField(blank=True, null=True)  # Date and time when complaint was resolved
    is_urgent = models.BooleanField(default=False)  # Flag to mark complaints as urgent
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='resolved_complaints')  # Admin who resolved the complaint

    def __str__(self):
        return self.title


class StatusHistory(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=2, choices=Complaint.STATUS_CHOICES)
    new_status = models.CharField(max_length=2, choices=Complaint.STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when status was updated

    def __str__(self):
        return f'{self.complaint.title} ({self.old_status} -> {self.new_status})'
