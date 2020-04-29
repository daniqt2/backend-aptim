# from django.shortcuts import render
from rest_framework import generics , authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer , AuthTokenSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """create auth token """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class ManageUserView(generics.RetrieveUpdateAPIView):
    """manage authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    """ return authenticated user"""
    def get_object(self):
        return self.request.user
        