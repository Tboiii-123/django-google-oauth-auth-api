from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from google_auth import views  # your app where the API view lives

urlpatterns = [
    # API endpoint for Google login
     path('google-login/', views.google_login, name='google-login'),
     path('user/', views.user_detail, name='user-detail'),
     
]


