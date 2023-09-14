from rest_framework import serializers

from .models import Person


def validate_name(value):
    """
    Validates if name is a string
    Validates if name already exists
    """
    if isinstance(value, str):
        queryset = Person.objects.filter(name__iexact=value)
        if queryset.exists():
            raise serializers.ValidationError(
                f'{value} is already a person name'
            )
        return value
    raise serializers.ValidationError('name must be a string')
