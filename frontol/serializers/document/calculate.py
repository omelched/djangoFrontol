from rest_framework import serializers

from frontol.src.libs.rest_framework.serializers import (
    FrontolInputSeralizer,
    FrontolOutputSerializer,
    CashierInformationBlockSerializer,
    PrintingInformationBlockSerializer,
)
from ..common import (
    PositionSerializer,
    ClientWithValidationCodeSerializer,
    ClientResultSerializer,
    ElectronicCheckSerializer,
    DocumentSerializer,
)


class CalculateOutputSerializer(FrontolOutputSerializer):

    client = ClientResultSerializer(
        required=False,
        allow_null=False,
    )
    electronicCheck = ElectronicCheckSerializer(
        required=False,
        allow_null=False,
    )
    document = DocumentSerializer(
        required=False,
        allow_null=False,
    )
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


class CalculateInputSerializer(FrontolInputSeralizer):
    client = ClientWithValidationCodeSerializer(
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
