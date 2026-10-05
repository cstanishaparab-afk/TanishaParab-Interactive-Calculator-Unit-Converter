def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")

    num1 = get_number("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ").strip()
    num2 = get_number("Enter second number: ")

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return

        result = num1 / num2

    else:
        print("Invalid operator.")
        return

    print("Result:", result)


def kilometers_to_miles():
    print("\n--- Kilometers to Miles ---")

    kilometers = get_number("Enter distance in kilometers: ")

    miles = kilometers * 0.621371

    print("Distance in miles:", miles)


def celsius_to_fahrenheit():
    print("\n--- Celsius to Fahrenheit ---")

    celsius = get_number("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in Fahrenheit:", fahrenheit)


def main():
    while True:
        print("\n==============================================")
        print("     INTERACTIVE CALCULATOR & UNIT CONVERTER")
        print("==============================================")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculator()

        elif choice == "2":
            print("\n--- Unit Converter ---")
            print("1. Kilometers to Miles")
            print("2. Celsius to Fahrenheit")
            print("3. Back to Main Menu")

            conversion_choice = input("Enter your choice: ").strip()

            if conversion_choice == "1":
                kilometers_to_miles()

            elif conversion_choice == "2":
                celsius_to_fahrenheit()

            elif conversion_choice == "3":
                continue

            else:
                print("Invalid choice. Please select 1, 2, or 3.")

        elif choice == "3":
            print("\nThank you for using the program!")
            print("Program closed successfully.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
