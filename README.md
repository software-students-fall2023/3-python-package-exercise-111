# LuhnChecker - Credit Card Validation and Generation

[![Build Status](https://github.com/software-students-fall2023/3-python-package-exercise-111/actions/workflows/build.yaml/badge.svg?event=pull_request)](https://github.com/software-students-fall2023/3-python-package-exercise-111/actions/workflows/build.yaml)

LuhnChecker is a Python library for validating, generating, and processing credit card numbers. This package provides a simple interface to implement the Luhn algorithm (also known as the mod 10 algorithm) which is widely used for validation of identification numbers.

## Features

- Validate credit card numbers using the Luhn algorithm.
- Generate valid credit card numbers for testing purposes.
- Mask credit card numbers for secure display.
- Determine the credit card issuer from the card number.

## Installation

To install LuhnChecker, simply use pip:

```bash
pip install luhnchecker

```

## Usage

Here's how to use LuhnChecker in your Python code:

### Validating a Credit Card Number

```python
from luhnchecker.luhn import Luhn

card_number = "1234567812345670"
if Luhn.check_luhn(card_number):
    print(f"{card_number} is a valid credit card number.")
else:
    print(f"{card_number} is an invalid credit card number.")
```

### Generating a Credit Card Number

```python
generated_card_number = Luhn.generate_luhn()
print(f"Generated card number: {generated_card_number}")
```

### Masking a Credit Card Number

```python
masked_number = Luhn.mask_card_number(card_number)
print(f"Masked card number: {masked_number}")
```

### Determining the Credit Card Issuer

```python
issuer = Luhn.credit_card_issuer(card_number)
print(f"The issuer of the card number {card_number} is {issuer}.")
```

## Contributing

We welcome contributions to LuhnChecker! Here's how you can set up the project for development:

1. Clone the repository:
   ```bash
   git clone https://github.com/software-students-fall2023/3-python-package-exercise-111
   ```
2. Navigate to the project directory:
   ```bash
   cd 3-python-package-exercise-111
   ```
3. Install the project along with its development dependencies using pipenv:
   ```bash
   pipenv install --dev
   ```
4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
5. Make changes and run the tests to ensure everything is working:
   ```bash
   pytest
   ```

## Team

- [Merlin Li](https://github.com/wwxihan2)
- [Steven](https://github.com/stevenkhl446)
- [Harley](https://github.com/harley-bulbasaur)
- [Zhiyi (Valery)](https://github.com/Val001z)
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.


## PyPI

LuhnChecker is also available through the Python Package Index (PyPI):

[luhnchecker on PyPI](https://pypi.org/project/luhnchecker/0.0.12/)
