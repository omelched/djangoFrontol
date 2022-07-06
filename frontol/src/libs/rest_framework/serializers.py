from rest_framework import serializers, exceptions


class FrontolInputSeralizer(serializers.Serializer):
    class CashierSerializer(serializers.Serializer):
        def update(self, instance, validated_data):
            pass

        def create(self, validated_data):
            pass

        code = serializers.IntegerField(
            required=True,
            allow_null=False,
        )
        name = serializers.CharField(
            required=True,
            allow_null=False,
            allow_blank=False,
        )
        text = serializers.CharField(
            required=True,
            allow_null=False,
            allow_blank=False,
        )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    dateTime = serializers.DateTimeField(
        required=True,
        allow_null=False,
    )
    organization = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    businessUnit = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    workPlace = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    cashier = CashierSerializer(
        required=True,
        allow_null=False,
    )


class FrontolOutputSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    code = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
    )
    error = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=True,
    )


class CashierInformationBlockSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    text = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    alignment = serializers.ChoiceField(
        choices=(
            'left',
            'center',
            'right',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    size = serializers.ChoiceField(
        choices=(
            'small',
            'medium',
            'large',
            'extralarge',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    weight = serializers.ChoiceField(
        choices=(
            'normal',
            'bold',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )


class PrintingInformationBlockSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):

        _type = getattr(self, 'print_type')
        if not _type:
            raise exceptions.ValidationError('<print_type> is required')

        if _type == 'text' and not getattr(self, 'text'):
            raise exceptions.ValidationError('for <type> = "text", <text> is required')

        elif _type == 'pair' and not all((getattr(self, 'left'), getattr(self, 'right'),)):
            raise exceptions.ValidationError('for <type> = "pair", <left> and <right> are required')

        elif _type in ('barcode', 'qrcode') and not getattr(self, 'data'):
            raise exceptions.ValidationError('for <type> = "barcode" | "qrcode", <data> is required')

        return super().validate(attrs)

    print_type = serializers.ChoiceField(
        choices=(
            'text',
            'pair',
            'line',
            'br',
            'barcode',
            'qrcode',
        ),
        required=True,
        allow_null=False,
        allow_blank=False,
        source='type',
    )

    # COMMON
    size = serializers.ChoiceField(
        choices=(
            'tiny',
            'default',
            'small',
            'medium',
            'large',
            'extralarge',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    alignment = serializers.ChoiceField(
        choices=(
            'left',
            'center',
            'right',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    wrapping = serializers.ChoiceField(
        choices=(
            'anywhere',
            'wordwrap',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    data = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=False,
    )

    # TEXT
    text = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=False,
    )

    # PAIR
    left = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    right = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=False,
    )
    separator = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=True,
        max_length=1,
    )

    # LINE
    symbol = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=True,
        max_length=1,
    )

    # BARCODE
    printText = serializers.ChoiceField(
        choices=(
            'none',
            'below',
            'above',
            'everywhere',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )

    # QRCODE
    correction = serializers.ChoiceField(
        choices=(
            'low',
            'medium',
            'high',
            'ultra',
        ),
        required=False,
        allow_null=False,
        allow_blank=False,
    )



