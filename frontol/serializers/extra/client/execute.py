from rest_framework import serializers

from frontol.src.libs.rest_framework.serializers import (
    FrontolInputSeralizer,
    FrontolOutputSerializer,
    CashierInformationBlockSerializer,
    PrintingInformationBlockSerializer,
)
from ...common import (
    ClientSerializer,
    ResponseValueSerializer,
)


class ExecuteOuputSerializer(FrontolOutputSerializer):
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


class ExecuteInputSerializer(FrontolInputSeralizer):
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
