from rest_framework import serializers

from apps.tasks.models import Tasks
from apps.labels.models import Labels
from apps.labels.serializers import LabelSerializer

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    labels = LabelSerializer(read_only=True, many=True)
    label_ids = serializers.PrimaryKeyRelatedField(queryset=Labels.objects.all(), write_only=True, many=True, source="labels")
    
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'is_complete', 'owner', 'labels', 'label_ids']
        
    def validate(self, data):
        request = self.context.get('request')
        labels = data.get('labels')
        for label in labels:
            if label.owner != request.user:
                raise serializers.ValidationError("No Label matches the given label id: {0}".format(label.id))  
        return data
        