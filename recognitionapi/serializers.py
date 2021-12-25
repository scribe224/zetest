from rest_framework import serializers

from .models import Recognition

class RecognitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recognition
        fields = ('status', 'text')