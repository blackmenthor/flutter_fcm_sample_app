from django.shortcuts import render
from .models import Food
from .serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class FoodViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset =  Food.objects.all()
    serializer_class = FoodSerializer
