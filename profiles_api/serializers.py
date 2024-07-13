from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing apiview"""
    name = serializers.CharField(max_length=10)
    username = serializers.CharField(max_length=4)
