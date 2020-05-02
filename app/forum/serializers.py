from rest_framework import serializers
from core.models import Channel, Topic, Thread, Comment, Event ,Club , ClubGroup

class ClubGroupSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField(read_only=True)
    created_at =serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = ClubGroup


class ChannelSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    club = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    get_topic_number = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Channel
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
   
    def get_topic_number(self, instance):
        return instance.topics.count()
    
class TopicSerializer(serializers.ModelSerializer):
    # channel = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    thread_number = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
     
    class Meta:
        model = Topic
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    def get_thread_number(self, instance):
        return instance.threads.count()
    
class ThreadSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    comment_number = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
     
    class Meta:
        model = Thread
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    def get_comment_number(self, instance):
        return instance.comments.count()

class CommentSerializer(serializers.ModelSerializer):
    # thread = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    created_at =serializers.SerializerMethodField(read_only=True)
    vote_number = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Comment
        exclude = ["updated_at"]
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    def get_vote_number(self, instance):
        return instance.votes.count()
    
class EventSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Event
        exclude = ["updated_at"]

class ClubSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    get_group_number = serializers.SerializerMethodField(read_only=True)
    get_member_number = serializers.SerializerMethodField(read_only=True)
    created_at =serializers.SerializerMethodField(read_only=True)
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_group_number(self, instance):
        return instance.groups.count()
    
    def get_member_number(self, instance):
        return instance.members.count()
    
    class Meta:
        model = Club
        exclude = ["updated_at"]
    

    