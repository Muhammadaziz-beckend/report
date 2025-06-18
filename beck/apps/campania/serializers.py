from rest_framework.serializers import ModelSerializer

from .models import *


class ListCampaniaSerializer(ModelSerializer):

    class Meta:
        model = Campania
        fields = (
            "id",
            "name",
            "amount_money",
            "owner",
        )


class CreateCampaniaSerializer(ModelSerializer):

    class Meta:
        model = Campania
        fields = (
            "id",
            "name",
            "amount_money",
            "owner",
        )