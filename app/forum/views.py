from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics , authentication, permissions
from forum.serializers import ChannelSerializer

from core.models import Channel , Topic , Thread , Comment
from .serializers import ChannelSerializer

from .signals import add_slug
from .permissions import isAuthorRO

# from core.utils import gen_random_str
# Create your views here.

# class ChannelView(generics.CreateAPIView):
#     queryset = Channel.objects.all()
#     permission_classes = [isAuthorRO]
#     serializer_class = ChannelSerializer
    
#     def perform_create(self,serializer):
#         serializer.save(club=self.request.user.club)
#         serializer.save(author=self.request.user)

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    lookup_field = "slug"
    serializer_class = ChannelSerializer
    
    def perform_create(self,serializer):
        serializer.save(club=self.request.user.club)
        serializer.save(author=self.request.user)
    
    # TOPICS 
class TopicView(generics.CreateAPIView):
    queryset = Topic.objects.all()
    permission_classes = [isAuthorRO]
    serializer_class = ChannelSerializer
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
        

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    
    
