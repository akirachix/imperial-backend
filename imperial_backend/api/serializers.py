from rest_framework import serializers
from fabric_price_catalogue.models import Agent

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'