from rest_framework import serializers


class GreetingSerializer(serializers.Serializer):
    message = serializers.CharField()
