from rest_framework import serializers

from frontol.src.libs.rest_framework.serializers import (
    FrontolInputSeralizer,
    FrontolOutputSerializer,
    CashierInformationBlockSerializer,
    PrintingInformationBlockSerializer
)
from ..common import (
    PositionSerializer,
    UntypedPaymentSerializer,
    ClientSerializer,
    PaymentSerializer,
)


class CancelBonusOutputSerializer(FrontolOutputSerializer):
    cashierInformation = serializers.ListField(
        child=CashierInformationBlockSerializer(
            allow_null=False,
        ),
        allow_null=False,
        allow_empty=True,
        required=False,
    )
    printingInformation = serializers.ListField(
        child=serializers.ListField(
            child=PrintingInformationBlockSerializer(
                allow_null=False,
            ),
            allow_null=False,
            allow_empty=False,
        ),
        allow_null=False,
        allow_empty=True,
        required=False,
    )


class CancelBonusInputSerializer(FrontolInputSeralizer):
    payment = UntypedPaymentSerializer(
        required=True,
        allow_null=False,
    )
    client = ClientSerializer(
        required=True,
        allow_null=False,
    )
    number = serializers.IntegerField(
        required=True,
        allow_null=False,
    )
    shift = serializers.IntegerField(
        required=True,
        allow_null=False,
    )
    uid = serializers.UUIDField(
        required=True,
        allow_null=False,
    )
    coupons = serializers.ListField(
        child=serializers.CharField(
            allow_null=False,
            allow_blank=False
        ),
        allow_null=False,
        allow_empty=True,
        required=True,
    )
    positions = serializers.ListField(
        child=PositionSerializer(
            allow_null=False,
        ),
        allow_null=False,
        allow_empty=False,
        required=True,
    )
    payments = serializers.ListField(
        child=PaymentSerializer(
            allow_null=False,
        ),
        allow_null=False,
        allow_empty=False,
        required=True,
    )
