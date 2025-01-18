from rest_framework import serializers

from apps.labels.models import Label

class LabelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')    
    
    class Meta:
        model = Label
        fields = ['id', 'name', 'owner']
        unique_together =  ('name', 'owner')
        