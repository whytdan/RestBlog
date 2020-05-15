from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from .serializers import (UserCreateSerialiazer, 
                          UserSerializer,)


User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerialiazer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)