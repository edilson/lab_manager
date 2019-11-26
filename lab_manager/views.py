from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers as serializers
from . import models as models

class LaboratoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LaboratorySerializer

    def get_queryset(self):
        return models.Laboratory \
            .objects \
            .filter(users=self.request.user) \
            .order_by('-created')

    def perform_create(self, serializer):
        laboratory = serializer.save()

        laboratory.users.add(self.request.user)