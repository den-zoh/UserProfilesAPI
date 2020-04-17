from django.urls import path
from userprofile.API.views import ProfileList

urlpatterns = [
    path("profiles/", ProfileList.as_view(), name='profile-list')

]