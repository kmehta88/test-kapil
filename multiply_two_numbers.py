def multiply_numbers(first, second):
    return first * second


def main():
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    product = multiply_numbers(first, second)
    print("Product:", product)


if __name__ == "__main__":
    main()
