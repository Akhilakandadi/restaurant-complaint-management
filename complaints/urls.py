from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('login/', auth_views.LoginView.as_view(template_name='complaints/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('success/', views.complaint_success, name='complaint_success'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('edit/<int:complaint_id>/', views.edit_complaint, name='edit_complaint'),
    path('delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
   
]

# Serve media files during development
if settings.DEBUG:  # Make sure this is inside the DEBUG block to ensure it's only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


