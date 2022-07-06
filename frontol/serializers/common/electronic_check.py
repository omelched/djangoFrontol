from rest_framework import serializers


class ElectronicCheckSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    form = serializers.ChoiceField(
        choices=(
            'electronicAndPrinted',
        ),
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    contact = serializers.ChoiceField(
        choices=(
            'email',
            'mobilePhone',
        ),
        required=True,
        allow_null=False,
        allow_blank=False,
    )
