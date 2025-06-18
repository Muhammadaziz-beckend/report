# from rest_framework.permissions import *
# from django.db.models.query import QuerySet

# from utils.mixins import UltraModelViewSet

# from .serializers import *
# from apps.campania.models import Campania as CampaniaModel



# class CampaniaModelViewSet(UltraModelViewSet):
#     queryset = CampaniaModel.objects.all()
#     lookup_field = "id"
#     serializer_class = ListCampaniaSerializer
#     serializer_classes = {
#         "list": ListCampaniaSerializer,
#         "retrieve": ListCampaniaSerializer,
#         "update": CreateCampaniaSerializer,
#         "create": CreateCampaniaSerializer,
#     }
#     permission_classes_by_action = {
#         "list": [IsAuthenticated],  # AllowAny IsAuthenticated
#         "retrieve": [IsAuthenticated],
#         "create": [IsAuthenticated, IsAdminUser],
#         "update": [IsAuthenticated, IsAdminUser],
#         "destroy": [IsAuthenticated, IsAdminUser],
#     }
    
#     def get_queryset(self):

#         queryset = self.queryset
#         if isinstance(queryset, QuerySet):
#             queryset = queryset.all()

#         user = self.request.user

#         if user.phone != "+996557230021":
#             queryset = queryset.filter(owner=user.campania)

#         return queryset