from django.urls import path ,include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


app_name = 'forum'

router = DefaultRouter()
router.register(r"channels", views.ChannelViewSet)


urlpatterns = [
    # path('channel/', views.ChannelView.as_view(), name='channel'),
    path('', include(router.urls)),
    # path('channel/<int:pk>/', snippet_highlight, name='snippet-highlight'),
]

