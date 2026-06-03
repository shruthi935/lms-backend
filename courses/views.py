from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer