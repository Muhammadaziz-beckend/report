from rest_framework.serializers import ModelSerializer

from .models import *


class ListObjectSerializer(ModelSerializer):

    class Meta:
        model = Object
        fields = (
            "id",
            "name",
            "campania",
            "creator",
        )


class CreateObjectSerializer(ModelSerializer):
    
    class Meta:
        model = Object
        fields = (
            "name",
        )