from django.shortcuts import render
from rest_framework import viewsets
from fabric_price_catalogue.models import Agent
from .serializers import AgentSerializer
# from fabric_price_catalogue import api

# Create your views here.
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

