from rest_framework import serializers
from backend.models import Text
 
class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'url', 'text', 'date')
