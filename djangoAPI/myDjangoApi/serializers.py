from rest_framework import serializers

from .models import Prof


class ProfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prof
        fields = ('name', 'field')
