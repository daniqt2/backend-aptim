from django.urls import path ,include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


app_name = 'forum'

router = DefaultRouter()
router.register(r"channels", views.ChannelViewSet)
router.register(r"topics", views.TopicViewSet)
router.register(r"threads", views.ThreadViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"events", views.EventViewSet)
router.register(r"clubs", views.ClubViewSet)
router.register(r"clubgroups", views.ClubGroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

