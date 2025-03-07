import pytest
from complaints.forms import ComplaintForm

def test_complaint_form_valid():
    form = ComplaintForm(data={
        'title': 'Late delivery',
        'description': 'Order took 2 hours to arrive',
        'email': 'user@example.com',      # Added required fields
        'category': 'SV',            # Make sure this exists in your choices
        'priority': 'HI',
    })
    assert form.is_valid()

def test_complaint_form_invalid_missing_fields():
    form = ComplaintForm(data={
        'title': 'Missing description'
    })
    assert not form.is_valid()  # Should fail because required fields are missing
