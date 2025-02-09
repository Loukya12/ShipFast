from django.urls import path
from .views import signup_view, signin_view, user_profile_view, status_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),  # Endpoint for user sign-up
    path('signin/', signin_view, name='signin'),  # Endpoint for user sign-in
    path('profile/', user_profile_view, name='profile'),  # Endpoint for user profile
    path('status/', status_view, name='status'),  # Endpoint for checking server status
]