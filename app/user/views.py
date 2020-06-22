# from django.shortcuts import render
from rest_framework import generics , authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from core.models import CustomUser
from rest_framework import viewsets
from rest_framework.settings import api_settings
from user.serializers import UserSerializer , AuthTokenSerializer ,UserUSerializer

# Create your views here.

# class UserPartialUpdateView(GenericAPIView, UpdateModelMixin):
#     '''
#     You just need to provide the field which is to be modified.
#     '''
#     queryset = CustomUser.objects.all()
#     serializer_class =serializer = UserSerializer

#     def put(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

class UserPartialUpdateView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter()
    serializer_class = UserUSerializer
    def get_queryset(self, request , id):
    #  id = self.request.GET.get('id')
     return CustomUser.objects.filter(user__pk=id)

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
    
class MUserView(generics.RetrieveUpdateAPIView):
    """manage authenticated user"""
    serializer_class = UserSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    
    """ return authenticated user"""
    def get_object(self,request,user_id):
        return CustomUser.objects.get(pk=user_id)
        