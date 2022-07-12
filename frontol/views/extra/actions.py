from frontol.src.actions import Action
from frontol.serializers import (
    DescribeInputSerializer,
    DescribeOuputSerializer,
    CheckOuputSerializer,
    CheckInputSerializer,
    ExecuteOuputSerializer,
    ExecuteInputSerializer,
)

describe = Action(
    name='describe',
    input_serializer_class=DescribeInputSerializer,
    output_serializer_class=DescribeOuputSerializer,
)
check = Action(
    name='check',
    input_serializer_class=CheckInputSerializer,
    output_serializer_class=CheckOuputSerializer,
)
execute = Action(
    name='execute',
    input_serializer_class=ExecuteInputSerializer,
    output_serializer_class=ExecuteOuputSerializer,
)
