from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from userprofile.models import Profile, ProfileStatus


class ProfileSerializer(ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)  # this is to enable someone to update one media file at a time

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)


class ProfileStatusSerializer(ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"

