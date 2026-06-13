from add_two_numbers import add_numbers
from multiply_two_numbers import multiply_numbers


def main():
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    total = add_numbers(first, second)
    product = multiply_numbers(first, second)

    print("Sum:", total)
    print("Product:", product)


if __name__ == "__main__":
    main()
