from rest_framework import serializers
from frontol.src.libs.phonenumbers import format_phone, InvalidNumber


class PhoneField(serializers.CharField):

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise serializers.ValidationError('Number must be a string')

        try:
            return format_phone(data)
        except InvalidNumber as e:
            raise serializers.ValidationError('Invalid number')