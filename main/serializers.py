from rest_framework import serializers
from .models import ImageModel

# class ImageUploadSerializer(serializers.Serializer):
#     image = serializers.ImageField(required=True) 

class ImageUploadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ImageModel
        fields = ['image']