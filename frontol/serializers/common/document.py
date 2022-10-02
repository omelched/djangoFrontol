from rest_framework import serializers


class DocumentSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

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

        discountAmount = serializers.DecimalField(
            max_digits=17,
            decimal_places=2,
            required=True,
            allow_null=False,
        )

    positions = serializers.ListField(
        child=PositionSerializer(
            allow_null=False,
        ),
        allow_null=False,
        allow_empty=True,
        required=False,
    )


class DocumentSerializerPaidAmount(DocumentSerializer):
    class PositionSerializer(DocumentSerializer.PositionSerializer):
        discountAmount = None
        paidAmount = serializers.DecimalField(
            max_digits=17,
            decimal_places=2,
            min_value=.0,
            required=True,
            allow_null=False,
        )

    positions = serializers.ListField(
        child=PositionSerializer(
            allow_null=False,
        ),
        allow_null=False,
        allow_empty=True,
        required=False,
    )
