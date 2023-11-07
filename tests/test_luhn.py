from luhnchecker.luhn import Luhn
import pytest


def test_generate_luhn_valid_length():
    for length in range(13, 20):
        card_number = Luhn.generate_luhn(length=length)
        # len(card_number) == length checks if the length of the generated number is as requested.
        # card_number.isdigit() ensures that the generated number contains only digit characters.
        assert len(card_number) == length and card_number.isdigit()


def test_generate_luhn_invalid_length():
    with pytest.raises(ValueError):
        Luhn.generate_luhn(length=10)


# This test generates a card number and then verifies it with the check_luhn method.
# If check_luhn returns True, the test passes.
def test_generate_luhn_passes_check():
    card_number = Luhn.generate_luhn()
    assert Luhn.check_luhn(card_number)

