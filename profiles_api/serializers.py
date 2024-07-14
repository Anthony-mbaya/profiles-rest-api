from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing apiview"""
    name = serializers.CharField(max_length=10)
    username = serializers.CharField(max_length=4)


class UserProfileSerializer(serializers.ModelSerializer):
    """"user profile serializers"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')#defines the fields to be serialized
        extra_kwargs = {
            'password':{
                'write_only':True,#user cannot get password
                'style':{'input_type':'password'}
            }
        }
    #our data is now validated got to create
    def create(self, validated_data):
        """create and return new user"""

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """handle updatign user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializing profile feed item"""
    class Meta:#to associate with profilefeeditem model
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile','status_text','created_on')
        extra_kwargs = { 'user_profile':{ 'read_only':True } }
