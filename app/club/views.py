from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics , authentication, permissions
from forum.serializers import ChannelSerializer,ThreadSerializer
from user.serializers import UserUSerializer,UserSerializer
from core.models import Channel , Topic , Thread , Comment ,Event, ClubGroup ,Club, CustomUser,EventAttendance, GroupMembership, MembershipRequest, Request
from .serializers import EventSerializer , ClubGroupSerializer ,ClubSerializer ,EventAttendanceSerializer, MembershipRequestSerializer,GroupMembershipSerializer, RequestSerializer

from forum.signals import add_slug
from forum.permissions import isAuthorRO


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    lookup_field = "id"
    serializer_class = ClubSerializer
    
    
class ClubGroupViewSet(viewsets.ModelViewSet):
    queryset = ClubGroup.objects.all()
    lookup_field = "id"
    serializer_class = ClubGroupSerializer
    
    # def perform_create(self,serializer):
    #     serializer.save(club=self.request.user.club)
    
class FocusGroupsViewSet(viewsets.ModelViewSet):
    queryset = ClubGroup.objects.filter()
    serializer_class = ClubGroupSerializer
    def get_queryset(self):
     club = self.request.GET.get('club')
     return ClubGroup.objects.filter(club__pk=club).order_by('created_at')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    lookup_field = "slug"
    serializer_class = EventSerializer
    
class FocusEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter()
    serializer_class = EventSerializer
    def get_queryset(self):
     club = self.request.GET.get('club')
     return Event.objects.filter(club__pk=club).order_by('created_at')
 
class ClubThreads(viewsets.ModelViewSet):
    queryset = Thread.objects.filter()
    serializer_class = ThreadSerializer
    def get_queryset(self):
     club = self.request.GET.get('club')
     return Thread.objects.filter(club__pk=club).order_by('created_at')
 
class EventAttendanceView(viewsets.ModelViewSet):
    queryset = EventAttendance.objects.filter()
    serializer_class = EventAttendanceSerializer
    
    def get_queryset(self):
     user = self.request.GET.get('user')
     return EventAttendance.objects.filter(person__pk=user).order_by('created_at')
 
class GroupMembershipView(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.filter()
    serializer_class = GroupMembershipSerializer
    
    def get_queryset(self):
     user = self.request.GET.get('user')
     return GroupMembership.objects.filter(person__pk=user).order_by('created_at')
 
class ClubMembershipRequestView(viewsets.ModelViewSet):
    queryset = MembershipRequest.objects.filter()
    serializer_class = MembershipRequestSerializer
    
    def get_queryset(self):
     user = self.request.GET.get('club')
     return MembershipRequest.objects.filter(club__pk=club).order_by('created_at')
 
class UserMembershipRequestView(viewsets.ModelViewSet):
    queryset = MembershipRequest.objects.filter()
    serializer_class = MembershipRequestSerializer
    
    def get_queryset(self):
     user = self.request.GET.get('user')
     return MembershipRequest.objects.filter(person__pk=user).order_by('created_at')
 
class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    lookup_field = "id"
    serializer_class = RequestSerializer
    
class UserRequestView(viewsets.ModelViewSet):
    queryset = Request.objects.filter()
    serializer_class = RequestSerializer
    
    def get_queryset(self):
     user = self.request.GET.get('user')
     return Request.objects.filter(user__pk=user).order_by('created_at')
 
class ClubRequestView(viewsets.ModelViewSet):
    queryset = Request.objects.filter()
    serializer_class = RequestSerializer
    
    def get_queryset(self):
     club = self.request.GET.get('club')
     return Request.objects.filter(club__pk=club).order_by('created_at')