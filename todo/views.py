from rest_framework import viewsets
from todo.serializers import (
    CategorySerializer,
    TaskSerializer,
    UserSerializer,
    TaskCategorySerializer,
)
from .models import Category, Task, TaskCategoryModel
from django.contrib.auth.models import User
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all().filter(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().filter(user=self.request.user)


class TaskCategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskCategorySerializer

    def get_queryset(self):
        return TaskCategoryModel.objects.all().filter(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
