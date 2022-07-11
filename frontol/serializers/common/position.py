from rest_framework import serializers


class PositionSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    index = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=1,
    )
    id = serializers.CharField(
        required=True,
        allow_null=False,
        source='position_id',
    )
    text = serializers.CharField(
        required=True,
        allow_null=False,
    )
    price = serializers.DecimalField(
        max_digits=17,
        decimal_places=2,
        min_value=.0,
        required=True,
        allow_null=False,
    )
    minimumPrice = serializers.DecimalField(
        max_digits=17,
        decimal_places=2,
        min_value=.0,
        required=True,
        allow_null=False,
    )
    quantity = serializers.DecimalField(
        max_digits=17,
        decimal_places=3,
        min_value=.0,
        required=True,
        allow_null=False,
    )
    totalAmount = serializers.DecimalField(
        max_digits=17,
        decimal_places=2,
        min_value=.0,
        required=True,
        allow_null=False,
    )
    coupons = serializers.ListField(
        child=serializers.CharField(
            allow_null=False,
            allow_blank=False
        ),
        allow_null=False,
        allow_empty=False,
        required=False,
    )


class PositionWithDiscardedAmount(PositionSerializer):
    discardedAmount = serializers.DecimalField(
        max_digits=17,
        decimal_places=2,
        min_value=.0,
        required=False,
        allow_null=False,
    )


class RefundedPosition(PositionWithDiscardedAmount):
    referenceIndex = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=1,
    )
    coupons = None
