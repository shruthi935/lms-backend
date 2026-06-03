from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    instructor_name = serializers.CharField(
        source="instructor.username",
        read_only=True
    )

    class Meta:
        model = Course
        fields = "__all__"