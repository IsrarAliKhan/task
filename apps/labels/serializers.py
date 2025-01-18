from rest_framework import serializers

from apps.labels.models import Labels

class LabelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model = Labels
        fields = ['id', 'name', 'owner']
    
    def validate(self, data):
        request = self.context.get('request')
        name = data.get('name')
        if Labels.objects.filter(owner=request.user, name=name):
            raise serializers.ValidationError("unique constraint failed: label {0} already exist".format(name))
        return data
    

class LabelNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Labels
        fields = ['name']
        