from rest_framework import serializers
from .models import Category, Task, TaskCategoryModel
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "user",
            "title",
            "description",
            "completed",
            "key",
            "time",
            "date",
            "date_created",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = "__all__"


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategoryModel
        fields = "__all__"
