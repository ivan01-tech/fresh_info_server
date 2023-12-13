from rest_framework import serializers
from .models import Information

class InformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
