import random

import luhnchecker.luhn


class Luhn:
    @staticmethod
    def _digits_of(n):
        # Helper method to split the number(string) into digits
        return [int(d) for d in str(n)]

    @staticmethod
    def check_luhn(card_number):
        """credit card number check with luhn algorithm."""
        card_number = card_number.replace(" ", "")

        digits = Luhn._digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(Luhn._digits_of(d * 2))
        return checksum % 10 == 0

    @staticmethod
    def generate_check_digit(number1):
        # Check if the input is an empty string
        if not number1:
            raise ValueError("Cannot generate a check digit from an empty string")
        # Check if the input is all digits
        if not number1.isdigit():
            raise ValueError("Input must be a numeric string")
        # Implementation of the Luhn algorithm to generate the check digit
        digits = Luhn._digits_of(number1)[::-1]

        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                doubled = digit * 2
                checksum += doubled - 9 if doubled > 9 else doubled
            else:
                checksum += digit
        # The check digit is the amount needed to make the sum a multiple of 10
        check_digit = (10 - (checksum % 10)) % 10
        return check_digit

    @staticmethod
    def validate_card_format(card_number):
        card_number = card_number.replace(" ", "")
        """Basic validation to check card number format."""
        return card_number.isdigit() and 13 <= len(card_number) <= 19

    @staticmethod
    def generate_luhn(length=16):
        # Generate a random, valid credit card number with a given length, default 16
        if length < 13 or length > 19:
            raise ValueError("Card number length must be between 13 and 19")

        # Generate a card number with length minus one
        card_number_without_check_digit = ''.join(str(random.randint(0, 9)) for _ in range(length - 1))

        # The check digit is what needs to be added to make the sum of the digits
        # a multiple of 10. Here we calculate it by constructing what the full card
        # number would be with a 0 in the check digit position, and then adjusting
        # the check digit until the whole number passes the Luhn check.
        for check_digit in range(10):
            if Luhn.check_luhn(card_number_without_check_digit + str(check_digit)):
                return card_number_without_check_digit + str(check_digit)

    @staticmethod
    def mask_card_number(card_number):
        """Masks a credit card number for safe display, removing spaces."""
        # Remove any spaces from the card number
        card_number_no_spaces = card_number.replace(" ", "")
        # Mask all but the last four characters
        masked_card = '*' * (len(card_number_no_spaces) - 4) + card_number_no_spaces[-4:]
        return masked_card

    @staticmethod
    def credit_card_issuer(card_number):
        card_number = card_number.replace(" ", "")
        if luhnchecker.luhn.Luhn.check_luhn(card_number):
            if card_number.startswith('4'):
                return 'Visa'
            elif any(card_number.startswith(str(i)) for i in range(51, 56)) or \
                    222100 <= int(card_number[:6]) <= 272099:
                return 'MasterCard'
            elif card_number.startswith(('34', '37')):
                return 'American Express'
            elif card_number.startswith('6011') or \
                    any(card_number.startswith(str(i)) for i in range(622126, 622926)) or \
                    any(card_number.startswith(str(i)) for i in range(644, 650)) or \
                    card_number.startswith('65'):
                return 'Discover'
            else:
                return 'Unknown'
        else:
            return 'invalid card number'

