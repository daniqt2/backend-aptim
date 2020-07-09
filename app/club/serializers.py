from rest_framework import serializers
from core.models import Channel, Topic, Thread, Comment, Event ,Club , ClubGroup, EventAttendance, GroupMembership,MembershipRequest,Request
from user.serializers import UserSerializer 
from forum.serializers import ChannelSerializer
from datetime import date

  
class RequestSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S") 
    
    class Meta:
        model = Request
        exclude = ["updated_at"]
          
class ClubGroupSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    created_at =serializers.SerializerMethodField(read_only=True)
    gmembers = UserSerializer(many=True,required=False)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = ClubGroup
        exclude = ["updated_at"]

class EventSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True,required=False)
    slug = serializers.SlugField(read_only=True)
    attendees = UserSerializer(many=True,required=False)
    week = serializers.SerializerMethodField(read_only=True)
    actual_week = serializers.SerializerMethodField(read_only=True)
    time= serializers.SerializerMethodField(read_only=True)
    
    def get_name(self , instance):
        return instance.title
    
    def get_time(self , instance):
        return instance.date.strftime("%H:%M:%S")
    
    def get_week(self , instance):
        return instance.date.strftime("%U")
    
    def get_actual_week(self , instance):
        return  date.today().strftime("%U")
    
    class Meta:
        model = Event
        exclude = ["updated_at"]

class ClubSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    get_group_number = serializers.SerializerMethodField(read_only=True)
    get_member_number = serializers.SerializerMethodField(read_only=True)
    created_at =serializers.SerializerMethodField(read_only=True)
    channels = ChannelSerializer(many=True,required=False)
    members = UserSerializer(many=True,required=False)
    requests = RequestSerializer(many=True,required=False)
    groups = ClubGroupSerializer(many=True,required=False)
    events = EventSerializer(many=True,required=False)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_group_number(self, instance):
        return instance.groups.count()
    
    def get_member_number(self, instance):
        return instance.members.count()
    
    class Meta:
        model = Club
        
        exclude = ["updated_at"]
        
class EventAttendanceSerializer(serializers.ModelSerializer):
    created_at =serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = EventAttendance
        
        exclude = ["updated_at"]
        
class GroupMembershipSerializer(serializers.ModelSerializer):
    created_at =serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    class Meta:
        model = GroupMembership
        
        exclude = ["updated_at"]
    
class MembershipRequestSerializer(serializers.ModelSerializer):
    created_at =serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = MembershipRequest
        
        exclude = ["updated_at"]
        
    
    
