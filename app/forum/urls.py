from django.urls import path ,include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


app_name = 'forum'

router = DefaultRouter()
router.register(r"channels", views.ChannelViewSet)
router.register(r"clubChannels", views.FocusChannelViewSet)
router.register(r"topics", views.TopicViewSet)
router.register(r"channelTopics", views.FocusTopicViewSet)
router.register(r"threads", views.ThreadViewSet)
router.register(r"topicThreads", views.FocusThreadViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"threadComments", views.FocusCommentViewSet)
router.register(r"users", views.UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
] 

