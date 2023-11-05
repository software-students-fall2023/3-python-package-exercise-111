import random


class Luhn:
    @staticmethod
    def _digits_of(n):
        # Helper method to split the number(string) into digits
        return [int(d) for d in str(n)]

    @staticmethod
    def check_luhn(card_number):
        """credit card number check with luhn algorithm."""

        digits = Luhn._digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(Luhn._digits_of(d * 2))
        return checksum % 10 == 0

    @staticmethod
    def generate_check_digit(card_number_without_check_digit):
        """Generate the final digit of a card number using the Luhn algorithm.
            ex. generate a random 14 digits and add a valid check digit to the 15th
            in order to pass the check_luhn.
        """
        digits = Luhn._digits_of(card_number_without_check_digit)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(Luhn._digits_of(d * 2))

        return (10 - (checksum % 10)) % 10

    @staticmethod
    def validate_card_format(card_number):
        """Basic validation to check card number format."""
        return card_number.isdigit() and 13 <= len(card_number) <= 19

    @staticmethod
    def generate_luhn(length=16):
        # Generate a random, valid credit card number with a given length, default 16
        if length < 13 or length > 19:
            raise ValueError("Card number length must be between 13 and 19")

        card_number = [random.randint(0, 9) for _ in range(length - 1)]
        card_number = [str(digit) for digit in card_number]
        card_number_without_check_digit = ''.join(card_number)
        check_digit = Luhn.generate_check_digit(card_number_without_check_digit)
        return card_number_without_check_digit + str(check_digit)


# The code below is not needed for the package but can be used for a simple CLI or tests
if __name__ == "__main__":
    # Example usage:
    card_numbers = ["49927398716", "49927398717", "1234567812345670", "1234567812345678"]

    for number in card_numbers:
        print(f"Card number {number} is", "valid." if Luhn.check_luhn(number) else "invalid.")
