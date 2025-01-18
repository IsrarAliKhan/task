from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.labels.models import Labels
from apps.labels.serializers import LabelSerializer
from apps.common.permissions import IsOwner

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Labels.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return Labels.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    