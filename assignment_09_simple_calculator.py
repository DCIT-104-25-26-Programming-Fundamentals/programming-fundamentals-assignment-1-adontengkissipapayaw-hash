# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def display_menu():
    print("\n" + "=" * 27)
    print("       SIMPLE CALCULATOR")
    print("=" * 27)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == '7':
            print("\nGoodbye!")
            break

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Error: Please enter a number between 1 and 7.")
            continue

        a = get_number("Enter first number : ")
        b = get_number("Enter second number: ")

        if choice == '1':
            result = add(a, b)
            op = '+'
        elif choice == '2':
            result = subtract(a, b)
            op = '-'
        elif choice == '3':
            result = multiply(a, b)
            op = '*'
        elif choice == '4':
            if b == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = divide(a, b)
            op = '/'
        elif choice == '5':
            if b == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = modulus(a, b)
            op = '%'
        elif choice == '6':
            result = exponentiate(a, b)
            op = '**'

        if isinstance(result, float) and choice != '4':
            # Show integer-like floats without trailing .0 when possible
            if result.is_integer():
                result_str = str(int(result))
            else:
                result_str = str(result)
        else:
            result_str = str(result)

        print(f"Result: {a} {op} {b} = {result_str}")


if __name__ == "__main__":
    main()

