from rest_framework.permissions import *
from django.db.models.query import QuerySet

from utils.mixins import UltraModelViewSet

from .serializers import *
from .models import *


class ObjectModelViewSet(UltraModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ListObjectSerializer
    lookup_field = "id"
    serializer_classes = {
        "list": ListObjectSerializer,
        "retrieve": ListObjectSerializer,
        "update": CreateObjectSerializer,
        "create": CreateObjectSerializer,
    }
    permission_classes_by_action = {
        "list": [IsAuthenticated],  # AllowAny IsAuthenticated
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, IsAdminUser],
        "update": [IsAuthenticated, IsAdminUser],
        "destroy": [IsAuthenticated, IsAdminUser],
    }

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        user = self.request.user

        if user.phone != "+996557230021":
            queryset = queryset.filter(campania=user.campania)

        return queryset
