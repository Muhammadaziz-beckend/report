from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.repo.views import *
from apps.object.views import *
from .ysge import swagger

router = DefaultRouter()
router.register("reports",ReportModelViewSet)
router.register("objects",ObjectModelViewSet)

urlpatterns = [
    #
    path("", include(router.urls)),
]

urlpatterns += swagger
