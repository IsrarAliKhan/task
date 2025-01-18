from rest_framework import serializers

from apps.tasks.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'is_complete', 'owner']
        