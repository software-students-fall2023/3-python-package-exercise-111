import luhnchecker.luhn
from luhnchecker.luhn import Luhn

luhnchecker.luhn.Luhn.generate_luhn()
test_card_numbers = {
    "Visa": "4111 1111 1111 1111",
    "MasterCard": "5555555555554444",
    "American Express": "378282246310005",
    "Discover": "6011 1111 1111 1117",
    "Invalid": "4111111111111112",
    "Unknown Issuer": "6414419214046251"
}


def main():
    for issuer, card_number in test_card_numbers.items():
        # Validate the card number
        validity = "valid" if Luhn.check_luhn(card_number) else "invalid"

        generated_card_number = Luhn.generate_luhn()

        masked_number = Luhn.mask_card_number(card_number)

        determined_issuer = Luhn.credit_card_issuer(card_number)

        print(f"Issuer: {issuer}")
        print(f"Card Number: {card_number} is a {validity} credit card number.")
        print(f"Generated card number: {generated_card_number}")
        print(f"Masked card number: {masked_number}")
        print(f"The determined issuer of the card number {card_number} is {determined_issuer}\n")


if __name__ == "__main__":
    main()
