from rest_framework import viewsets

from apps.labels.models import Label
from apps.labels.serializers import LabelSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    