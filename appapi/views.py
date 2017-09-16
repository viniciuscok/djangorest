from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PizzaSerialazer
from .models import Pizza
# Create your views here.

class PizzaViewApi(viewsets.ModelViewSet):
    queryset = Pizza.objects.all().order_by("name")
    serializer_class = PizzaSerialazer