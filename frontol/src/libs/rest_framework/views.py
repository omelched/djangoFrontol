from rest_framework import views, status, response, request
from .authentication import FrontolTokenAuthentication


class FrontolAPIView(views.APIView):
    input_serializer_class = None
    output_serializer_class = None
    authentication_classes = (
        FrontolTokenAuthentication,
    )

    def post(self, _request: request.Request, *args, **kwargs):
        serializer = self.get_serializer(data=_request.data, mode='input')
        serializer.is_valid(raise_exception=True)

        result = self.execute_action(serializer)

        return response.Response(result.data, status=status.HTTP_200_OK)

    def execute_action(self, serializer):
        raise NotImplementedError

    def get_serializer(self, mode: str, *args, **kwargs):
        serializer_class = self.get_serializer_class(mode)
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self, mode: str):
        return getattr(self, f'{mode}_serializer_class')

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
