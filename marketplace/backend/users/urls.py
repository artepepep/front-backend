from django.urls import path
from .views import LatestUsersView

urlpatterns = [
    path('api/v1/users/<int:counter>/', LatestUsersView.as_view(), name='fix-latest-users'),
]