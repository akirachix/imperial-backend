from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Value as V, CharField, F

from users.models import Trader, Agent, RecyclingCompany
from .serializers import TraderSerializer, AgentSerializer, RecyclingCompanySerializer

class UserUnionList(APIView):
    def get(self, request):
        traders = Trader.objects.annotate(
            user_type=V('trader', output_field=CharField())
        ).values(
            'id', 'name', 'gender', 'market_name', 'phone_number', 'date_enrolled', 'user_type'
        )
        agents = Agent.objects.annotate(
            user_type=V('agent', output_field=CharField())
        ).values(
            'id', 'name', 'date_of_birth', 'gender', 'assigned_market', 'phone_number', 'user_type'
        )
        recycling_companies = RecyclingCompany.objects.annotate(
            user_type=V('recycling_company', output_field=CharField())
        ).values(
            'id', 'company_name', 'address', 'phone_number', 'email', 'licence_number', 'user_type'
        )
        combined = list(traders) + list(agents) + list(recycling_companies)
        return Response(combined)

    def post(self, request):
        user_type = request.data.get('user_type')
        if user_type == 'trader':
            serializer = TraderSerializer(data=request.data)
        elif user_type == 'agent':
            serializer = AgentSerializer(data=request.data)
        elif user_type == 'recycling_company':
            serializer = RecyclingCompanySerializer(data=request.data)
        else:
            return Response({'error': 'Unknown user_type'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user_type = request.data.get('user_type')
        if user_type == 'trader':
            try:
                user = Trader.objects.get(pk=pk)
            except Trader.DoesNotExist:
                return Response({'error': 'Trader not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = TraderSerializer(user, data=request.data, partial=True)
        elif user_type == 'agent':
            try:
                user = Agent.objects.get(pk=pk)
            except Agent.DoesNotExist:
                return Response({'error': 'Agent not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = AgentSerializer(user, data=request.data, partial=True)
        elif user_type == 'recycling_company':
            try:
                user = RecyclingCompany.objects.get(pk=pk)
            except RecyclingCompany.DoesNotExist:
                return Response({'error': 'RecyclingCompany not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = RecyclingCompanySerializer(user, data=request.data, partial=True)
        else:
            return Response({'error': 'Invalid user_type'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_type = request.data.get('user_type')
        if user_type == 'trader':
            try:
                user = Trader.objects.get(pk=pk)
            except Trader.DoesNotExist:
                return Response({'error': 'Trader not found'}, status=status.HTTP_404_NOT_FOUND)
            user.delete()
        elif user_type == 'agent':
            try:
                user = Agent.objects.get(pk=pk)
            except Agent.DoesNotExist:
                return Response({'error': 'Agent not found'}, status=status.HTTP_404_NOT_FOUND)
            user.delete()
        elif user_type == 'recycling_company':
            try:
                user = RecyclingCompany.objects.get(pk=pk)
            except RecyclingCompany.DoesNotExist:
                return Response({'error': 'RecyclingCompany not found'}, status=status.HTTP_404_NOT_FOUND)
            user.delete()
        else:
            return Response({'error': 'Invalid user_type'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
