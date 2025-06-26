
from rest_framework import serializers
from users.models import Trader, Agent, RecyclingCompany


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class RecyclingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecyclingCompany
        fields = '__all__'


class UserUnionSerializer(serializers.Serializer):
    first_name =serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    user_type = serializers.CharField()        
