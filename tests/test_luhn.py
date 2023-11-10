import pytest
from luhnchecker.luhn import Luhn


class Tests:
    def test_generate_luhn_valid_length(self):
        for length in range(13, 20):
            card_number = Luhn.generate_luhn(length=length)
            # Check if the length of the generated number is as requested.
            assert len(card_number) == length, f"Expected length {length}, but got {len(card_number)}"
            # Ensure that the generated number contains only digit characters.
            assert card_number.isdigit(), f"Generated card number '{card_number}' contains non-digit characters"

    def test_generate_luhn_invalid_length(self):
        with pytest.raises(ValueError) as excinfo:
            Luhn.generate_luhn(length=10)
        assert "Card number length must be between 13 and 19" in str(
            excinfo.value), "ValueError does not contain the correct message"

    def test_generate_luhn_passes_check(self):
        card_number = Luhn.generate_luhn()
        is_valid = Luhn.check_luhn(card_number)
        # If check_luhn returns True, the test passes. If not, print the card number.
        assert is_valid, f"Generated card number {card_number} failed the Luhn check"

    # ----->check_luhn<-----#
    # this is to check the check_luhn function in luhn.py works properly with valid number.
    def test_check_luhn_valid(self):
        valid_luhn_number = "4532015112830366"  # this number is arbitrary, but it has to be a valid number.
        assert Luhn.check_luhn(valid_luhn_number), f"The Luhn number {valid_luhn_number} should be valid."

    # this is to check the check_luhn function in luhn.py works properly with invalid number.
    def test_check_luhn_invalid(self):
        # Test with a known invalid Luhn number.
        invalid_luhn_number = "4532015112830367"  # this number is arbitrary, but it has to be a invalid number.
        assert not Luhn.check_luhn(invalid_luhn_number), f"The Luhn number {invalid_luhn_number} should be invalid."

    # this is to check the check_luhn function in luhn.py works properly with non numeric number.
    def test_check_luhn_non_numeric(self):
        # Test with a non-numeric input, expecting a failure.
        non_numeric_luhn_number = "4532a1511283b366"  # this number is arbitrary, but it has to be a non numeric number.
        with pytest.raises(ValueError) as excinfo:
            Luhn.check_luhn(non_numeric_luhn_number)
        assert "invalid literal for int()" in str(excinfo.value), "A ValueError should be raised for non-numeric input."

    # ----->check_luhn<-----#

    # ----->generate_check_digit<-----#

    def test_generate_check_digit_creates_valid_luhn(self):
        # Take a known number without its Luhn check digit
        number_without_check_digit = "7992739871"  # A number that needs a Luhn check digit
        # Generate the check digit
        check_digit = Luhn.generate_check_digit(number_without_check_digit)
        # Verify the entire number is now a valid Luhn number
        full_number = number_without_check_digit + str(check_digit)
        assert Luhn.check_luhn(
            full_number), f"The generated check digit does not create a valid Luhn number: {full_number}"

    def test_generate_check_digit_with_non_numeric_input(self):
        # Verify that non-numeric input raises an error
        non_numeric_input = "12345a"
        with pytest.raises(ValueError) as excinfo:
            Luhn.generate_check_digit(non_numeric_input)
        assert "Input must be a numeric string" in str(
            excinfo.value), "A ValueError should be raised for non-numeric input."

    def test_generate_check_digit_with_empty_string(self):
        # Verify that an empty string raises an error or behaves as expected
        with pytest.raises(ValueError) as excinfo:
            Luhn.generate_check_digit("")
        # Here we assume that generate_check_digit method raises a ValueError for an empty string
        # adapt the expected error message if your method behaves differently
        assert "Cannot generate a check digit from an empty string" in str(
            excinfo.value), "A ValueError should be raised for an empty input."

    # ----->generate_check_digit<-----#

    # ----->credit_card_issuer<-----#

    def test_issuer_visa(self):
        visa_card = '4111111111111111'  # A known Visa pattern
        assert Luhn.credit_card_issuer(visa_card) == 'Visa', "The issuer should be Visa."

    def test_issuer_mastercard(self):
        mastercard_card = '5500000000000004'  # A known MasterCard pattern
        assert Luhn.credit_card_issuer(mastercard_card) == 'MasterCard', "The issuer should be MasterCard."

    def test_issuer_amex(self):
        amex_card = '341111111111111'  # A known American Express pattern
        assert Luhn.credit_card_issuer(amex_card) == 'American Express', "The issuer should be American Express."

    # ----->credit_card_issuer<-----#

    # ----->mask_card_number<-----#
    # this is to check the mask_card_number function in luhn.py works properly with valid number.
    def test_mask_card_number(self):
        # Test masking a valid card number with space
        card_with_space = '1234 5678 9012 3456'
        assert Luhn.mask_card_number(card_with_space) == '************3456'

        # Test masking a card number with no spaces
        card_without_space = '1234567890123456'
        assert Luhn.mask_card_number(card_without_space) == '************3456'

        # Test masking an empty string
        card_empty = ''
        assert Luhn.mask_card_number(card_empty) == ''

    # ----->mask_card_number<-----#
