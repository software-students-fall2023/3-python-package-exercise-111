# src/luhnchecker/__main__.py
import sys
from .luhn import Luhn


def print_menu():
    print("Welcome to Luhn Checker CLI")
    print("1. Check a card number")
    print("2. Generate check digit")
    print("3. Validate card format")
    print("4. Generate a card number")
    print("5. Exit")
    print("Enter your choice (1-5):")


def main():
    while True:
        print_menu()
        choice = input()

        if choice == '1':
            card_number = input("Enter the card number to check: ")
            if Luhn.check_luhn(card_number):
                print(f"{card_number} is a valid card number.")
            else:
                print(f"{card_number} is not a valid card number.")
        elif choice == '2':
            card_number_without_check_digit = input("Enter the card number without check digit: ")
            check_digit = Luhn.generate_check_digit(card_number_without_check_digit)
            print(f"The check digit for {card_number_without_check_digit} is {check_digit}.")
        elif choice == '3':
            card_number = input("Enter the card number to validate: ")
            if Luhn.validate_card_format(card_number):
                print(f"{card_number} has a valid format.")
            else:
                print("Invalid card format.")
        elif choice == '4':
            length = input("Enter the length of the card number to generate (13-19): ")
            try:
                length = int(length)
                generated_card = Luhn.generate_luhn(length)
                print(f"Generated card number: {generated_card}")
            except ValueError:
                print("Invalid input. Please enter a number between 13 and 19.")
        elif choice == '5':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
