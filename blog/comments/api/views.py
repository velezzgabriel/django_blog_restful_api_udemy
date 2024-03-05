from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializers import CommentSerializer

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering=['created_at'] # ordena ascendente. This is for OrderingFilter
    # ordering=['-created_at'] # ordena descendente. This is for OrderingFilter

    filterset_fields = ['post']
