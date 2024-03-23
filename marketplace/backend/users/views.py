from users.models import User
from .serializers import LatestUsersSerializer
from rest_framework import generics

class LatestUsersView(generics.ListAPIView):
    serializer_class = LatestUsersSerializer

    def get_queryset(self):
        counter = self.kwargs.get('counter', 10)
        return User.objects.all().order_by('-date_joined')[:counter]