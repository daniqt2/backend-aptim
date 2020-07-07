from rest_framework import serializers
from core.models import Channel, Topic, Thread, Comment
from user.serializers import UserSerializer 
from datetime import date

        

class CommentSerializer(serializers.ModelSerializer):
    # thread = serializers.StringRelatedField(read_only=True)
    # user = serializers.StringRelatedField(read_only=True)
    created_at =serializers.SerializerMethodField(read_only=True)
    # vote_number = serializers.SerializerMethodField(read_only=True,required=False)
    slug = serializers.SlugField(read_only=True)
    writter=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Comment
        exclude = ["updated_at"]
    
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    # def get_vote_number(self, instance):
    #     return (instance.votes.count())
    
    def get_writter(self, instance):
        return instance.user.username
    

class ThreadSerializer(serializers.ModelSerializer):
    # name = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    comment_number = serializers.SerializerMethodField(read_only=True)
    # like_number =  serializers.SerializerMethodField(read_only=True,required=False)
    slug = serializers.SlugField(read_only=True)
    comments = CommentSerializer(many=True,required=False)
    writter = serializers.SerializerMethodField(read_only=True)
    actual_week = serializers.SerializerMethodField(read_only=True)
    week = serializers.SerializerMethodField(read_only=True)
    date =  serializers.SerializerMethodField(read_only=True)

     
    class Meta:
        model = Thread
        exclude = ["updated_at"]
        
        
    def get_date(self , instance):
        return instance.created_at.strftime("%Y-%m-%d")
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%d-%m-%Y %H:%M:%S")
    
    def get_comment_number(self, instance):
        return instance.comments.count()
    
    def get_writter(self, instance):
        return instance.creator.username
    
    def get_week(self , instance):
        return instance.created_at.strftime("%U")
    
    def get_actual_week(self , instance):
        return  date.today().strftime("%U")
    # def get_like_number(self, instance):
    #     return (instance.likes.count())
        
        
class TopicSerializer(serializers.ModelSerializer):
    # channel = serializers.StringRelatedField(read_only=True)
    # name = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    thread_number = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    threads = ThreadSerializer(many=True,required=False)
     
    class Meta:
        model = Topic
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    def get_thread_number(self, instance):
        return instance.threads.count()
        
class ChannelSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    get_topic_number = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    topics = TopicSerializer(many=True,required=False)
    
    class Meta:
        model = Channel
        exclude = ["updated_at"]
         
    def get_created_at(self , instance):
        return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
   
    def get_topic_number(self, instance):
        return instance.topics.count()
    
# class ClubGroupSerializer(serializers.ModelSerializer):
#     slug = serializers.SlugField(read_only=True)
#     created_at =serializers.SerializerMethodField(read_only=True)
#     gmembers = UserSerializer(many=True,required=False)
    
#     def get_created_at(self , instance):
#         return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
#     class Meta:
#         model = ClubGroup
#         exclude = ["updated_at"]

# class EventSerializer(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField(read_only=True,required=False)
#     slug = serializers.SlugField(read_only=True)
#     attendees = UserSerializer(many=True,required=False)
#     week = serializers.SerializerMethodField(read_only=True)
#     actual_week = serializers.SerializerMethodField(read_only=True)
#     time= serializers.SerializerMethodField(read_only=True)
    
#     def get_name(self , instance):
#         return instance.title
    
#     def get_time(self , instance):
#         return instance.date.strftime("%H:%M:%S")
    
#     def get_week(self , instance):
#         return instance.date.strftime("%U")
    
#     def get_actual_week(self , instance):
#         return  date.today().strftime("%U")
    
#     class Meta:
#         model = Event
#         exclude = ["updated_at"]

# class ClubSerializer(serializers.ModelSerializer):
#     slug = serializers.SlugField(read_only=True)
#     get_group_number = serializers.SerializerMethodField(read_only=True)
#     get_member_number = serializers.SerializerMethodField(read_only=True)
#     created_at =serializers.SerializerMethodField(read_only=True)
#     channels = ChannelSerializer(many=True,required=False)
#     members = UserSerializer(many=True,required=False)
#     groups = ClubGroupSerializer(many=True,required=False)
#     events = EventSerializer(many=True,required=False)
    
#     def get_created_at(self , instance):
#         return instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
#     def get_group_number(self, instance):
#         return instance.groups.count()
    
#     def get_member_number(self, instance):
#         return instance.members.count()
    
#     class Meta:
#         model = Club
        
#         exclude = ["updated_at"]
        
# class EventAttendanceSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = EventAttendance
        
#         exclude = ["updated_at"]
    
# class EventAttendanceSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = EventAttendance
        
#         exclude = ["updated_at"]
    