from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    
    lookup_field = 'slug'
    
    queryset = Category.objects.all()  #option 1
    # queryset = Category.objects.filter(published=True)  #option 2

    # option 3 thisone needs a queryset that could be either opt#1 or opt#2	
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']