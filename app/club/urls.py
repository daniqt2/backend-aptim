from django.urls import path ,include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


app_name = 'club'

router = DefaultRouter()
router.register(r"events", views.EventViewSet)
router.register(r"clubEvents", views.FocusEventViewSet)
router.register(r"clubs", views.ClubViewSet)
router.register(r"clubGroups", views.FocusGroupsViewSet)
router.register(r"clubgroups", views.ClubGroupViewSet)
router.register(r"eventAttendance", views.EventAttendanceView)
router.register(r"clubRequests", views.ClubMembershipRequestView)
router.register(r"userRequests", views.UserMembershipRequestView)
router.register(r"userGroups", views.GroupMembershipView)
router.register(r"requests", views.RequestView)
router.register(r"request", views.ClubRequestView)
router.register(r"userRequest", views.UserRequestView)
# router.register(r"userRequest", views.UserRequestView)
# router.register(r"clubRequest", views.ClubRequestView)




urlpatterns = [
    path('', include(router.urls)),
] 
