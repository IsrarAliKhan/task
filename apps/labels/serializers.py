from rest_framework import serializers

from apps.labels.models import Labels

class LabelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')    
    
    class Meta:
        model = Labels
        fields = ['id', 'name', 'owner']
        