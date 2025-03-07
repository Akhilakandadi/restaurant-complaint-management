import pytest
from complaints.models import Complaint
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_complaint():
    user = User.objects.create_user(username='testuser', password='password')
    complaint = Complaint.objects.create(
        user=user,
        title="Test Complaint",
        description="This is a test complaint."
    )
    assert complaint.get_status_display() == "Pending"

    assert complaint.title == "Test Complaint"
    assert str(complaint) == "Test Complaint"  # If you have __str__ defined
