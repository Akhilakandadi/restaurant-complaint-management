import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from complaints.models import Complaint

@pytest.mark.django_db
def test_submit_complaint_authenticated(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    response = client.post(reverse('submit_complaint'), {
        'title': 'Food was cold',
        'description': 'Ordered biryani but it was cold',
        'email': 'testuser@example.com',  # Added required fields
        'category': 'SV',       # Update to match your choices
        'priority': 'HI',
        'is_urgent': False,
    })

    assert response.status_code == 302 # Should redirect to dashboard or success page

@pytest.mark.django_db
def test_dashboard_view_authenticated(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    response = client.get(reverse('user_dashboard'))

    assert response.status_code == 200
    assert b"Your Complaints" in response.content  # Adjusted to match actual template

@pytest.mark.django_db
def test_dashboard_shows_complaints(client):
    user = User.objects.create_user(username='testuser', password='password')
    Complaint.objects.create(
        user=user,
        title="Slow Service",
        description="It took over an hour to get our food."
    )

    client.login(username='testuser', password='password')

    response = client.get(reverse('user_dashboard'))
    assert response.status_code == 200
    assert b"Slow Service" in response.content  # Complaint should appear in dashboard
