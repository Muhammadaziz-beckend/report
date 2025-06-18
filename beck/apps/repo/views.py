from rest_framework.permissions import *

from django.db.models.query import QuerySet
from utils.mixins import UltraModelViewSet
from utils.paginations import PaginatorClass
from .serializers import *

from .models import *


class ReportModelViewSet(UltraModelViewSet):
    queryset = Report.objects.all()
    lookup_field = "id"
    serializer_class = ListReportSerializer
    serializer_classes = {
        "list": ListReportSerializer,
        "retrieve": RetrReportSerializer,
        "update": CreateReportSerializer,
        "create": CreateReportSerializer,
    }
    permission_classes_by_action = {
        "list": [IsAuthenticated],  # AllowAny IsAuthenticated
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, IsAdminUser],
        "update": [IsAuthenticated, IsAdminUser],
        "destroy": [IsAuthenticated, IsAdminUser],
    }
    pagination_class = PaginatorClass

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        user = self.request.user

        if user.is_superuser:
            return queryset

        queryset = queryset.filter(owner=user)

        return queryset
