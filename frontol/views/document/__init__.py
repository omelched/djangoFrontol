from rest_framework import exceptions

from frontol.src.libs.rest_framework.views import FrontolAPIView
from .actions import calculate, pay_by_bonus, cancel_bonus_payment, confirm, refund

ACTIONS = {
    'calculate_receipt': calculate,
    'payByBonus_receipt': pay_by_bonus,
    'cancelBonusPayment_receipt': cancel_bonus_payment,
    'confirm_receipt': confirm,
    'confirm_refundReceipt': refund,
}


class DocumentAPIView(
    FrontolAPIView,
):
    # fuck whoever thinks this RESTless hell is integration-friendly
    action = None

    def get_serializer(self, mode: str, *args, **kwargs):
        if mode == 'input':
            if not {'action', 'type'}.issubset(kwargs['data'].keys()):
                raise exceptions.ParseError(f'No <action> or <type> was provided')

            self.action = ACTIONS[f"{kwargs['data'].pop('action')}_{kwargs['data'].pop('type')}"]

            if not self.action:
                raise exceptions.ParseError(f'No <action> or <type> was provided')

        return super().get_serializer(mode, *args, **kwargs)

    def get_serializer_class(self, mode: str):
        return getattr(self.action, f'{mode}_serializer_class')

    def execute_action(self, serializer):

        result = self.action.execute(serializer.data)
        result_serializer = self.get_serializer(mode='output', data=result)
        result_serializer.is_valid(raise_exception=True)

        return result_serializer
