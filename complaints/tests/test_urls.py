from django.urls import reverse, resolve
from complaints.views import submit_complaint, user_dashboard

def test_submit_complaint_url():
    url = reverse('submit_complaint')
    assert resolve(url).func == submit_complaint

def test_user_dashboard_url():
    url = reverse('user_dashboard')
    assert resolve(url).func == user_dashboard
