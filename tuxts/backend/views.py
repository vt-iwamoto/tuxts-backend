from rest_framework import viewsets
from backend.models import Text
from backend.serializers import TextSerializer
from django_filters.rest_framework import DjangoFilterBackend
 
class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    filterset_fields = ('date',)
