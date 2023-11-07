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
        assert "Card number length must be between 13 and 19" in str(excinfo.value), "ValueError does not contain the correct message"

    def test_generate_luhn_passes_check(self):
        card_number = Luhn.generate_luhn()
        is_valid = Luhn.check_luhn(card_number)
        # If check_luhn returns True, the test passes. If not, print the card number.
        assert is_valid, f"Generated card number {card_number} failed the Luhn check"
