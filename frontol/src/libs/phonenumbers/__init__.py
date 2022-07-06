import phonenumbers as _phonenumbers


class InvalidNumber(Exception):
    pass


def format_phone(phone: str) -> str:
    try:
        number = _phonenumbers.parse(phone, region="RU")
    except _phonenumbers.NumberParseException:
        raise InvalidNumber()

    # will be like +79998887766
    result = _phonenumbers.format_number(number, _phonenumbers.PhoneNumberFormat.E164)

    return result
