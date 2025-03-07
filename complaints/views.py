# complaints/views.py
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import ComplaintForm  # assuming your complaint form is already set up
from django.contrib import messages
from .models import Complaint

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('submit_complaint')  # Redirect to the complaint submission page
    else:
        form = UserRegistrationForm()
    return render(request, 'complaints/register.html', {'form': form})



# View to handle complaint form (only for logged-in users)
@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user  # associate complaint with logged-in user
            complaint.status = 'PE'  # Ensure status is always set to Pending
            complaint.save()
            return redirect('complaint_success')  # After submission, redirect to a success page
    else:
        form = ComplaintForm()
    return render(request, 'complaints/submit_complaints.html', {'form': form})

#User Dashboard (Read - View User's Own Complaints)
@login_required
def user_dashboard(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'complaints/user_dashboard.html', {'complaints': complaints})

# Edit Complaint (Update)
@login_required
def edit_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)

    if complaint.status != 'PE':
        messages.error(request, "You can't edit a complaint that is already being processed.")
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint updated successfully.')
            return redirect('user_dashboard')
    else:
        form = ComplaintForm(instance=complaint)

    return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})

# Delete Complaint (Delete)
@login_required
def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id, user=request.user)

    if complaint.status != 'PE':
        messages.error(request, "You can't delete a complaint that is already being processed.")
        return redirect('user_dashboard')

    if request.method == 'POST':
        complaint.delete()
        messages.success(request, 'Complaint deleted successfully.')
        return redirect('user_dashboard')

    return render(request, 'complaints/confirm_delete.html', {'complaint': complaint})



# Success page after submitting a complaint
def complaint_success(request):
    return render(request, 'complaints/success.html')
