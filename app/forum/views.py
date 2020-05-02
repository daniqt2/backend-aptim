from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics , authentication, permissions
from forum.serializers import ChannelSerializer

from core.models import Channel , Topic , Thread , Comment ,Event, ClubGroup ,Club
from .serializers import ChannelSerializer ,TopicSerializer,ThreadSerializer,\
    CommentSerializer,EventSerializer , ClubGroupSerializer ,ClubSerializer

from .signals import add_slug
from .permissions import isAuthorRO

# Create your views here.

# class ChannelView(generics.CreateAPIView):
#     queryset = Channel.objects.all()
#     permission_classes = [isAuthorRO]
#     serializer_class = ChannelSerializer
    
#     def perform_create(self,serializer):
#         serializer.save(club=self.request.user.club)
#         serializer.save(author=self.request.user)

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    lookup_field = "slug"
    serializer_class = ClubSerializer
    
    
class ClubGroupViewSet(viewsets.ModelViewSet):
    queryset = ClubGroup.objects.all()
    lookup_field = "slug"
    serializer_class = ClubGroupSerializer
    
    def perform_create(self,serializer):
        serializer.save(club=self.request.user.club)


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    lookup_field = "slug"
    serializer_class = ChannelSerializer
    
    def perform_create(self,serializer):
        serializer.save(club=self.request.user.club)
        serializer.save(author=self.request.user)
    
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    lookup_field = "slug"
    serializer_class = TopicSerializer
    
class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    lookup_field = "slug"
    serializer_class = ThreadSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    lookup_field = "slug"
    serializer_class = CommentSerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    lookup_field = "slug"
    serializer_class = EventSerializer
    
    def perform_create(self,serializer):
        serializer.save(club=self.request.user.club)
    

    
