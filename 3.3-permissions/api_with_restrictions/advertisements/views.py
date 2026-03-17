from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import PermissionDenied

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AdvertisementFilter
    ordering_fields = ['created_at', 'price']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        # Проверяем, что текущий пользователь - автор
        if self.get_object().author != self.request.user:
            raise PermissionDenied("Нельзя редактировать чужое объявление")
        serializer.save()
    
    def perform_destroy(self, instance):
        # Проверяем, что текущий пользователь - автор
        if instance.author != self.request.user:
            raise PermissionDenied("Нельзя удалить чужое объявление")
        instance.delete()
    
    def get_throttles(self):
        if self.request.user.is_authenticated:
            self.throttle_scope = 'user'
        else:
            self.throttle_scope = 'anon'
        from rest_framework.throttling import ScopedRateThrottle
        return [ScopedRateThrottle()]