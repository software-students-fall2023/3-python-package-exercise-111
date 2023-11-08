from luhnchecker.luhn import Luhn


def display_menu():
    print("\nMenu:")
    print("1. Check a credit card number (Luhn check)")
    print("2. Generate a check digit for a number")
    print("3. Validate the format of a credit card number")
    print("4. Generate a random valid credit card number")
    print("5. Mask a credit card number for safe display")
    print("6. Determine the issuer of a credit card")
    print("7. Exit")
    choice = input("Choose an option (1-7): ")
    return choice


def main():
    while True:
        choice = display_menu()

        if choice == '1':
            card_number = input("Enter the credit card number to check: ")
            if Luhn.check_luhn(card_number):
                print("The credit card number is valid according to the Luhn algorithm.")
            else:
                print("The credit card number is NOT valid.")

        elif choice == '2':
            number = input("Enter the number to generate a check digit for: ")
            try:
                check_digit = Luhn.generate_check_digit(number)
                print(f"The check digit is: {check_digit}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            card_number = input("Enter the credit card number to validate: ")
            if Luhn.validate_card_format(card_number):
                print("The credit card number format is valid.")
            else:
                print("The credit card number format is NOT valid.")

        elif choice == '4':
            length = input("Enter the length of the credit card number to generate (13-19): ")
            try:
                length = int(length)
                card_number = Luhn.generate_luhn(length)
                print(f"The generated credit card number is: {card_number}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            card_number = input("Enter the credit card number to mask: ")
            masked_card = Luhn.mask_card_number(card_number)
            print(f"The masked credit card number is: {masked_card}")

        elif choice == '6':
            card_number = input("Enter the credit card number to determine its issuer: ")
            issuer = Luhn.credit_card_issuer(card_number)
            print(f"The issuer of the credit card is: {issuer}")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
