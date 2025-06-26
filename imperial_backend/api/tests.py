from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Trader, Agent, RecyclingCompany
from rest_framework import status

class TraderAPITestCase(APITestCase):
    def setUp(self):
        self.trader = Trader.objects.create(
            name="Alice Trader",
            gender="Female",
            market_name="Central Market",
            phone_number="0711111111",
            date_enrolled="2025-01-01"
        )
        self.list_url = reverse('users-list')

    def test_trader_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(u.get('name') == self.trader.name and u.get('user_type') == 'trader' for u in response.data))

    def test_trader_create(self):
        data = {
            "user_type": "trader",
            "name": "Bob Trader",
            "gender": "Male",
            "market_name": "West Market",
            "phone_number": "0722222222",
            "date_enrolled": "2025-06-01"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Trader.objects.filter(name="Bob Trader").exists())

class AgentAPITestCase(APITestCase):
    def setUp(self):
        self.agent = Agent.objects.create(
            name="John Agent",
            date_of_birth="1990-05-15",
            gender="Male",
            assigned_market="East Market",
            phone_number="0733333333"
        )
        self.list_url = reverse('users-list')
        self.detail_url = reverse('users-detail', args=[self.agent.pk])

    def test_agent_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(u.get('name') == self.agent.name and u.get('user_type') == 'agent' for u in response.data))

    def test_agent_create(self):
        data = {
            "user_type": "agent",
            "name": "Jane Agent",
            "date_of_birth": "1995-08-20",
            "gender": "Female",
            "assigned_market": "North Market",
            "phone_number": "0744444444"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Agent.objects.filter(name="Jane Agent").exists())

    def test_agent_patch(self):
        data = {
            "user_type": "agent",
            "phone_number": "0799999999"
        }
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agent.refresh_from_db()
        self.assertEqual(self.agent.phone_number, "0799999999")

    def test_agent_delete(self):
        data = {"user_type": "agent"}
        response = self.client.delete(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Agent.objects.filter(pk=self.agent.pk).exists())

class RecyclingCompanyAPITestCase(APITestCase):
    def setUp(self):
        self.company = RecyclingCompany.objects.create(
            company_name="Eco Recycle",
            address="123 Green Lane",
            phone_number="0755555555",
            email="eco@recycle.com",
            licence_number="LIC98765"
        )
        self.list_url = reverse('users-list')
        self.detail_url = reverse('users-detail', args=[self.company.pk])

    def test_company_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(u.get('company_name') == self.company.company_name and u.get('user_type') == 'recycling_company' for u in response.data))

    def test_company_create(self):
        data = {
            "user_type": "recycling_company",
            "company_name": "Green Cycle",
            "address": "456 Blue Ave",
            "phone_number": "0766666666",
            "email": "green@cycle.com",
            "licence_number": "LIC12345"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(RecyclingCompany.objects.filter(company_name="Green Cycle").exists())

    def test_company_patch(self):
        data = {
            "user_type": "recycling_company",
            "address": "789 New Address"
        }
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.address, "789 New Address")

    def test_company_delete(self):
        data = {"user_type": "recycling_company"}
        response = self.client.delete(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(RecyclingCompany.objects.filter(pk=self.company.pk).exists())
