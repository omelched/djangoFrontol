from rest_framework import serializers, exceptions
from frontol.src.libs.rest_framework.fields import PhoneField


class ClientSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        if 'mobilePhone' not in attrs and 'card' not in attrs:
            raise exceptions.ValidationError('<mobilePhone> or <card> is required')

        return super().validate(attrs)

    mobilePhone = PhoneField(
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    card = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=False,
    )


class ClientWithValidationCodeSerializer(ClientSerializer):
    validationCode = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )


class ClientResultSerializer(ClientWithValidationCodeSerializer):
    def validate(self, attrs):
        return super(ClientSerializer, self).validate(attrs)

    email = serializers.EmailField(
        required=False,
    )
    card = None
    availableAmount = serializers.DecimalField(
        max_digits=17,
        decimal_places=2,
        min_value=.0,
        required=False,
        allow_null=False,
    )
