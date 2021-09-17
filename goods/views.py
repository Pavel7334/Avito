import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from goods.models import Ads
from goods.serializers import AvitoSerializer


class AdsViewSet(ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AvitoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price', 'created_at']
    search_fields = ['name', 'price', 'category__title']
    ordering_fields = ['price', 'created_at', 'category__title']
    category__title = django_filters.CharFilter(lookup_expr='icontains')

    def get_object(self):
        ad = super().get_object()
        ad.view += 1
        ad.save()
        self.view = ad.view
        return ad

