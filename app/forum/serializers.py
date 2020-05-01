from rest_framework import serializers
from core.models import Channel, Topic, Thread, Comment

class ChannelSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    title = serializers.StringRelatedField(read_only=True)
    club = serializers.StringRelatedField(read_only=True)
    description = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    get_topic_number = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Channel
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
   
    def get_topic_number(self, instance):
        return instance.topics.count()
    
class  TopicSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(read_only=True)
    channel = serializers.StringRelatedField(read_only=True)
    description = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    thread_number = serializers.SerializerMethodField(read_only=True)
     
    class Meta:
        model = Topic
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    def get_thread_number(self, instance):
        return instance.topics.count()
     