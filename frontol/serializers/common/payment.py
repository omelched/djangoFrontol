from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    type = serializers.ChoiceField(
        choices=(
            'bonus',
        ),
        required=True,
        allow_null=False,
    )
    mode = serializers.ChoiceField(
        choices=(
            'nonFiscal',
        ),
        required=True,
        allow_null=False,
    )
    amount = serializers.DecimalField(
        max_digits=17,
        decimal_places=2,
        min_value=.0,
        required=True,
        allow_null=False,
    )


class UntypedPaymentSerializer(PaymentSerializer):
    type = None
