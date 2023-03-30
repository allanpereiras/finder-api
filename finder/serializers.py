from rest_framework import serializers

from . import models


class FindingSerializer(serializers.ModelSerializer):
    """Serializer for Finding model"""

    class Meta:
        model = models.Finding
        fields = "__all__"
