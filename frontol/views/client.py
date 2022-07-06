from django.apps import apps

from frontol.src.libs.rest_framework.views import FrontolAPIView
from frontol.serializers import ClientInputSerializer, ClientOutputSerializer

FRONTOLAPP_CONFIG = apps.get_app_config('frontol')


class ClientAPIView(FrontolAPIView):
    input_serializer_class = ClientInputSerializer
    output_serializer_class = ClientOutputSerializer

    def execute_action(self, serializer):
        result = FRONTOLAPP_CONFIG.external_actions_parser('client')(serializer.data)
        result_serializer = self.get_serializer(mode='output', data=result)
        result_serializer.is_valid(raise_exception=True)

        return result_serializer



