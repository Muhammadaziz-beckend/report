from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.account.views import Login
from apps.repo.views import *
from apps.object.views import *
from apps.campania.views import *
from .ysge import swagger

router = DefaultRouter()
router.register("reports",ReportModelViewSet)
router.register("objects",ObjectModelViewSet)
# router.register("campania",CampaniaModelViewSet)

urlpatterns = [
    # auth
    path("auth/login", Login.as_view()),
    #
    path("", include(router.urls)),
]

urlpatterns += swagger
