from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """
        test api view
    """
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as funcitons (get, post, put, patch, delete)',
            'similar to traditioanl django view',
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview':an_apiview})