"""
Provides filtering backends that can be used to filter the results
returned by list views.

Filtering is done mostly using the package django_filters integrated with DRF.
"""

from django_filters import rest_framework as filters

from . import models


class FindingFilter(filters.FilterSet):
    """Provides attributes for filtering results of the Finding model."""

    scans = filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = models.Finding
        fields = ["definition_id"]