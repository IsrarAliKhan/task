from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.labels.models import Labels

class LabelSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())  
    
    class Meta:
        model = Labels
        fields = ['id', 'name', 'owner']
        validators = [
            UniqueTogetherValidator(
                queryset=Labels.objects.all(), 
                fields=('name', 'owner')
            )
        ] 
        