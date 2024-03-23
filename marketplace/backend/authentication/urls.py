from django.urls import path
from .views import GoogleLoginApi

urlpatterns = [
      path("api/v1/auth/login/google/", GoogleLoginApi.as_view(), name="login-with-google"),
]