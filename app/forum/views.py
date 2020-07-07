from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics , authentication, permissions
from forum.serializers import ChannelSerializer
from user.serializers import UserUSerializer,UserSerializer
from core.models import Channel , Topic , Thread , Comment ,Event, ClubGroup ,Club, CustomUser
from .serializers import ChannelSerializer ,TopicSerializer,ThreadSerializer,\
    CommentSerializer

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


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    lookup_field = "id"
    serializer_class = UserUSerializer
    

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.filter()
#     serializer_class = UserUSerializer
#     def get_queryset(self):
#      id = self.request.GET.get('id')
#      return CustomUser.objects.filter(id=id)


# class ClubViewSet(viewsets.ModelViewSet):
#     queryset = Club.objects.all()
#     lookup_field = "id"
#     serializer_class = ClubSerializer
    
    
# class ClubGroupViewSet(viewsets.ModelViewSet):
#     queryset = ClubGroup.objects.all()
#     lookup_field = "slug"
#     serializer_class = ClubGroupSerializer
    
#     # def perform_create(self,serializer):
#     #     serializer.save(club=self.request.user.club)
    
# class FocusGroupsViewSet(viewsets.ModelViewSet):
#     queryset = ClubGroup.objects.filter()
#     serializer_class = ClubGroupSerializer
#     def get_queryset(self):
#      club = self.request.GET.get('club')
#      return ClubGroup.objects.filter(club__pk=club).order_by('created_at')


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    lookup_field = "slug"
    serializer_class = ChannelSerializer
    
    # def perform_create(self,serializer):
    #     serializer.save(club=self.request.user.club)
    #     serializer.save(author=self.request.user)
    
class FocusChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.filter()
    serializer_class = ChannelSerializer
    def get_queryset(self):
     club = self.request.GET.get('club')
     return Channel.objects.filter(club__pk=club).order_by('created_at')
    
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    lookup_field = "slug"
    serializer_class = TopicSerializer
    
class FocusTopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.filter()
    serializer_class = TopicSerializer
    def get_queryset(self):
     channel = self.request.GET.get('channel')
     return Topic.objects.filter(channel__pk=channel).order_by('created_at')
    
class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    lookup_field = "slug"
    serializer_class = ThreadSerializer
    
class FocusThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.filter()
    serializer_class = ThreadSerializer
    def get_queryset(self):
     topic = self.request.GET.get('topic')
     return Thread.objects.filter(topic__pk=topic).order_by('created_at')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    lookup_field = "slug"
    serializer_class = CommentSerializer
    
class FocusCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer
    def get_queryset(self):
     thread = self.request.GET.get('thread')
     return Comment.objects.filter(thread__pk=thread).order_by('created_at')
    
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     lookup_field = "slug"
#     serializer_class = EventSerializer
    
# class FocusEventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.filter()
#     serializer_class = EventSerializer
#     def get_queryset(self):
#      club = self.request.GET.get('club')
#      return Event.objects.filter(club__pk=club).order_by('created_at')
 
# class ClubThreads(viewsets.ModelViewSet):
#     queryset = Thread.objects.filter()
#     serializer_class = ThreadSerializer
#     def get_queryset(self):
#      club = self.request.GET.get('club')
#      return Thread.objects.filter(club__pk=club).order_by('created_at')
 
# class EventAttendanceView(viewsets.ModelViewSet):
#     queryset = EventAttendance.objects.filter()
#     serializer_class = EventAttendanceSerializer
    
#     def get_queryset(self):
#      user = self.request.GET.get('user')
#      return EventAttendance.objects.filter(person__pk=user).order_by('created_at')
    
    

    
