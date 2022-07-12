from frontol.src.libs.rest_framework.views import ActionBasedFrontolAPIView
from .actions import calculate, pay_by_bonus, cancel_bonus_payment, confirm, refund


class DocumentAPIView(ActionBasedFrontolAPIView):
    actions = {
        'calculate_receipt': calculate,
        'payByBonus_receipt': pay_by_bonus,
        'cancelBonusPayment_receipt': cancel_bonus_payment,
        'confirm_receipt': confirm,
        'confirm_refundReceipt': refund,
    }
