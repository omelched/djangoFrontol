from rest_framework import serializers

from frontol.src.libs.rest_framework.serializers import (
    FrontolInputSeralizer,
    FrontolOutputSerializer,
)
from ...common import (
    ClientSerializer,
    ResponseValueSerializer,
)


class CheckOuputSerializer(FrontolOutputSerializer):
    class ValidationCodeSerializer(serializers.Serializer):
        def update(self, instance, validated_data):
            pass

        def create(self, validated_data):
            pass

        validationCode = serializers.CharField(
            required=False,
            allow_null=False,
            allow_blank=False,
        )

    client = ValidationCodeSerializer(
        required=False,
        allow_null=False,
    )


class CheckInputSerializer(FrontolInputSeralizer):

    client = ClientSerializer(
        required=True,
        allow_null=False,
    )
    values = serializers.ListField(
        child=ResponseValueSerializer(
            allow_null=False
        ),
        allow_empty=False,
        allow_null=False,
    )
