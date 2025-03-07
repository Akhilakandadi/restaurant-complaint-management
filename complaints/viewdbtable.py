import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Now setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_complaint_system.settings')
import django
django.setup()

# Now you can import models from complaints
from complaints.models import Complaint
from tabulate import tabulate

# Query the database to get all complaints
complaints = Complaint.objects.all()

# Prepare the data to be displayed (convert the queryset to a list of values)
complaint_list = [
    [complaint.description, complaint.title, complaint.category, complaint.submitted_at]
    for complaint in complaints
]

# Define the headers for the table
headers = ["Description", "Title", "Category", "Submitted At"]

# Display the complaints in a pretty table
print(tabulate(complaint_list, headers=headers, tablefmt="pretty"))
