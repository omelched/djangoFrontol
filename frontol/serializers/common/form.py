from rest_framework import serializers


class ResponseValueSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    value = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=True,
    )


class FormSerializer(serializers.Serializer):
    class TitleSerializer(serializers.Serializer):
        def update(self, instance, validated_data):
            pass

        def create(self, validated_data):
            pass

        text = serializers.CharField(
            required=False,
            allow_null=False,
            allow_blank=False,
        )

    class FormElementSerializer(serializers.Serializer):
        class ComboBoxItemSerializer(serializers.Serializer):

            def update(self, instance, validated_data):
                pass

            def create(self, validated_data):
                pass

            value = serializers.CharField(
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

        type = serializers.ChoiceField(
            choices=(
                'label',
                'inputLine',
                'comboBox',
            ),
            required=True,
            allow_null=False,
            allow_blank=False,
        )

        # LABEL
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
        weight = serializers.ChoiceField(
            choices=(
                'normal',
                'bold',
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

        # INPUTLINE
        name = serializers.CharField(
            required=False,
            allow_null=False,
            allow_blank=False,
        )
        text = serializers.CharField(
            required=False,
            allow_null=False,
            allow_blank=False,
        )
        default = serializers.CharField(
            required=False,
            allow_null=False,
            allow_blank=True,
        )
        regExp = serializers.CharField(
            required=False,
            allow_null=False,
            allow_blank=False,
        )

        # comboBox
        items = serializers.ListField(
            child=ComboBoxItemSerializer(
                allow_null=False,
            ),
            required=False,
            allow_null=False,
            allow_empty=False,
        )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    title = TitleSerializer(
        required=False,
        allow_null=False,
    )
    elements = serializers.ListField(
        child=FormElementSerializer(
            allow_null=False,
        ),
        required=False,
        allow_null=False,
        allow_empty=False,
    )
