from django.urls import path ,include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


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
router.register(r"events", views.EventViewSet)
router.register(r"clubEvents", views.FocusEventViewSet)
router.register(r"clubs", views.ClubViewSet)
router.register(r"clubGroups", views.FocusGroupsViewSet)
router.register(r"clubgroups", views.ClubGroupViewSet)
router.register(r"users", views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

