def add_numbers(first, second):
    return first + second


def main():
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    total = add_numbers(first, second)
    print("Sum:", total)


if __name__ == "__main__":
    main()
