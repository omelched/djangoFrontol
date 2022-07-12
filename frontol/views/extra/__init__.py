from frontol.src.libs.rest_framework.views import ActionBasedFrontolAPIView
from .actions import describe, check, execute


class ExtraClientAPIView(ActionBasedFrontolAPIView):
    actions = {
        'describe': describe,
        'check': check,
        'execute': execute,
    }
