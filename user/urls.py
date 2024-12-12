from django.urls import path
from rest_framework.urls import app_name

from .views import UserCreateView, UserDetailView


app_name = 'user'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('details/<int:pk>/', UserDetailView.as_view(), name='detail'),
]
