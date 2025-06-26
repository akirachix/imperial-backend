
from django.urls import path
from .views import UserUnionList

urlpatterns = [
    path('users/', UserUnionList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserUnionList.as_view(), name='users-detail'),
]
