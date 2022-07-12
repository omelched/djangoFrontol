from frontol.src.libs.rest_framework.serializers import (
    FrontolInputSeralizer,
    FrontolOutputSerializer,
)
from ...common import (
    ClientSerializer,
    FormSerializer
)


class DescribeOuputSerializer(FrontolOutputSerializer):
    form = FormSerializer(
        required=True,
        allow_null=False,
    )


class DescribeInputSerializer(FrontolInputSeralizer):
    client = ClientSerializer(
        required=True,
        allow_null=False,
    )
