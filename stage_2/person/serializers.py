from rest_framework import serializers

from .models import Person
from .validators import validate_name


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Person
        fields = [
            'id',
            'name'
        ]
