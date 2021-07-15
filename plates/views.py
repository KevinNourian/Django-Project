from django.shortcuts import render
from rest_framework import viewsets
from .models import Plate
from .serializers import PlateSerializer


class PlateView(viewsets.ModelViewSet):
	queryset = Plate.objects.all()
	serializer_class = PlateSerializer






