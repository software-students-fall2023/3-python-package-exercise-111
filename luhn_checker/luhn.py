# luhnchecker/luhn.py

class Luhn:
    @staticmethod
    def check_luhn(card_number):
        """credit card number check with luhn algorithm."""
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10 == 0

    @staticmethod
    def generate_check_digit(card_number_without_check_digit):
        """Generate the final digit of a card number using the Luhn algorithm.
            ex. generate a random 14 digits and add a valid check digit to the 15th
            in order to pass the check_luhn.
        """
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number_without_check_digit)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))

        return (10 - (checksum % 10)) % 10

    @staticmethod
    def validate_card_format(card_number):
        """Basic validation to check card number format."""
        return card_number.isdigit() and 13 <= len(card_number) <= 19

# The code below is not needed for the package but can be used for a simple CLI or tests
if __name__ == "__main__":
    # Example usage:
    card_numbers = ["49927398716", "49927398717", "1234567812345670", "1234567812345678"]
    
    for number in card_numbers:
        print(f"Card number {number} is", "valid." if Luhn.check_luhn(number) else "invalid.")
