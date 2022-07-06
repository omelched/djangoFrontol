from frontol.src.actions import Action
from frontol.serializers import (
    CalculateInputSerializer,
    CalculateOutputSerializer,
    CancelBonusInputSerializer,
    CancelBonusOutputSerializer,
    ConfirmReceiptInputSerializer,
    ConfirmReceiptOutputSerializer,
    ConfirmRefundReceiptInputSerializer,
    ConfirmRefundReceiptOutputSerializer,
    PayByBonusInputSerializer,
    PayByBonusOutputSerializer
)

calculate = Action(
    name='calculate_receipt',
    input_serializer_class=CalculateInputSerializer,
    output_serializer_class=CalculateOutputSerializer
)
pay_by_bonus = Action(
    name='payByBonus_receipt',
    input_serializer_class=PayByBonusInputSerializer,
    output_serializer_class=PayByBonusOutputSerializer
)
cancel_bonus_payment = Action(
    name='cancelBonusPayment_receipt',
    input_serializer_class=CancelBonusInputSerializer,
    output_serializer_class=CancelBonusOutputSerializer
)
confirm = Action(
    name='confirm_receipt',
    input_serializer_class=ConfirmReceiptInputSerializer,
    output_serializer_class=ConfirmReceiptOutputSerializer,
)
refund = Action(
    name='confirm_refundReceipt',
    input_serializer_class=ConfirmRefundReceiptInputSerializer,
    output_serializer_class=ConfirmRefundReceiptOutputSerializer,
)
