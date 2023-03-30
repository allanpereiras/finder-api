from django_filters import rest_framework as drf_filter
from rest_framework import viewsets

from . import filters, models, serializers


class FindingViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides default `list()`, `retrieve()` actions for Finding model."""

    queryset = models.Finding.objects.all()
    serializer_class = serializers.FindingSerializer
    filter_backends = (drf_filter.DjangoFilterBackend,)
    filterset_class = filters.FindingFilter
