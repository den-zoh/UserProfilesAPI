from django.urls import include, path
from userprofile.API.views import (ProfileViewSet,
                                   ProfileStatusViewSet,
                                   AvatarUpdateView)
from rest_framework.routers import DefaultRouter

# This is when one uses viewsets.
# profile_list = ProfileViewSet.as_view({"get": "list"})
# profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

# Example using the router now
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewSet, basename="status")


urlpatterns = [
    # ----- THE TWO PATTERNS WORK WITH THE VIEWSETS ABOVE ------#
    # path("profiles/", profile_list, name='profile-list'),
    # path("profiles/<int:pk>", profile_detail, name='profile-detail')
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")

]