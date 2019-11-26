from .models import *
from rest_framework import serializers

class LaboratorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            'id',
            'name',
            'typo',
            'location',
        )