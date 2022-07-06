from django.apps import apps
from rest_framework import serializers

FRONTOLAPP_CONFIG = apps.get_app_config('frontol')


class Action:
    input_serializer_class: serializers.Serializer = None
    output_serializer_class: serializers.Serializer = None
    name: str = None

    def __init__(
            self,
            input_serializer_class,
            output_serializer_class,
            name: str,
    ):
        self.input_serializer_class = input_serializer_class
        self.output_serializer_class = output_serializer_class
        self.name = name

    def _preaction(self, _input):
        ...
        return _input

    def _postaction(self, _input, _output):
        ...
        return _output

    def execute(self, _input) -> dict:
        _input = self._preaction(_input)
        _output = FRONTOLAPP_CONFIG.external_actions_parser(self.name)(_input)
        _output = self._postaction(_input, _output)

        return _output
