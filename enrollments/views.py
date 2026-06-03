from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentListView(generics.ListCreateAPIView):

    queryset = Enrollment.objects.all()

    serializer_class = EnrollmentSerializer