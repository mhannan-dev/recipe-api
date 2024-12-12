from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserCreateSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
