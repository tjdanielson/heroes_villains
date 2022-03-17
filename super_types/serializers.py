from rest_framework import serializers
from .models import SuperType


class SuperTypeSerializer(serializers.Serializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']