from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
# for permissions
from rest_framework.authentication import TokenAuthentication

# for login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken 
from . import serializers
# for user profile view set
from . import models
# for permissions
from . import permmissions

# Create your views here.

class HelloApiView(APIView):
    """
        test api view
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as funcitons (get, post, put, patch, delete)',
            'similar to traditioanl django view',
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """
            Create a nello message with oour name
        """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {0}".format(name)
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
            Handles updating an object
        """
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """
            Patch request, only updates fields provided in the reeeequest
        """
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """
            Deletes an object
        """
        return Response({'method': 'patch'})

class HelloViewSet(viewsets.ViewSet):
    """
        Test Api ViewSet
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
            Return a hello message
        """
        a_viewset = [
            'Uses actions (list, create, retreive, partial_updtae)' ,
            'Automatically map URLS using Routers'
        ]
        return Response({'message': 'Hello!','a_viewset':a_viewset})

    def create(self, requeset):
        """
            Create a new hello message
        """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retreive(self, request, pk=None):
        """
            Handles getting an object by it's ID
        """
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """
            Handles updating an object
        """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """
            Handles updating part of an object 
        """
        return Response({'http_method': 'PATCH'})

    def delete(self, request, pk=None):
        """
            Deletes an object
        """
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """
        Handles creating and  updating profiles
    """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permmissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """
        Checks email and password and returns an auth token
    """
    serializer_class = AuthTokenSerializer
    def create(self, request):
        """
            Use the ObtainAuthToken APIView to validata and create a token
        """
        return ObtainAuthToken().post(request)


