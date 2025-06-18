from rest_framework.serializers import ModelSerializer

from .models import *


class ListReportSerializer(ModelSerializer):

    class Meta:
        model = Report
        fields = (
            "id",
            "title",
            "type_repo",
            "owner",
            "amoute",
            "_object",
        )


class RetrReportSerializer(ModelSerializer):

    class Meta:
        model = Report
        fields = (
            "id",
            "title",
            "type_repo",
            "owner",
            "amoute",
            "_object",
        )
        
        
class CreateReportSerializer(ModelSerializer):

    class Meta:
        model = Report
        fields = (
            "title",
            "type_repo",
            "amoute",
            "_object",
        )
        