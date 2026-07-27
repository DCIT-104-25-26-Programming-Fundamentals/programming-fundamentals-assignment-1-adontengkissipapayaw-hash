# =============================================================================
# Array Statistics — Friendly Calculator
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# This program asks how many numbers you'd like to enter, prompts for each
# one, then prints a friendly summary showing the sum, average, maximum and
# minimum. Each calculation is implemented in its own function.
#
# NOTES:
# - Enter a positive integer for the count. If you enter 0 or a negative
#   number the program will stop and show an error.
# - Do not use Python's built-in `sum()`, `max()`, or `min()` in the
#   calculation functions — implement them using loops as required.
#
# =============================================================================
# YOUR CODE BELOW — implement the required functions and `main()`
# =============================================================================


def compute_sum(numbers):
    """Return the sum of the numbers using a loop (no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def compute_average(numbers):
    """Return the average of the numbers. Assumes len(numbers) > 0."""
    total = compute_sum(numbers)
    return total / len(numbers)


def compute_max(numbers):
    """Return the maximum value using a loop (no built-in max())."""
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val


def compute_min(numbers):
    """Return the minimum value using a loop (no built-in min())."""
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val


def _format_number(x):
    """Format numbers for display: integers without .0, floats trimmed."""
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    if isinstance(x, float):
        # show at most one decimal place for friendliness
        return str(round(x, 1)).rstrip('0').rstrip('.')
    return str(x)


def _format_average(x):
    """Format average specially: one decimal when needed."""
    return _format_number(x)


def main():
    try:
        n_input = input("How many numbers would you like to enter? ")
        n = int(n_input)
    except ValueError:
        print("Error: please enter a whole number for the count (e.g. 5).")
        return

    if n <= 0:
        print("Error: please enter a positive integer greater than zero.")
        return

    numbers = []
    for i in range(1, n + 1):
        try:
            val = input(f"Please enter number {i}: ")
            # accept integer or float
            if '.' in val:
                num = float(val)
            else:
                num = int(val)
        except ValueError:
            print("Error: please enter a valid number (e.g. 4 or 3.5).")
            return
        numbers.append(num)

    total = compute_sum(numbers)
    avg = compute_average(numbers)
    maximum = compute_max(numbers)
    minimum = compute_min(numbers)

    print("\nResults:")
    print(f"Sum:     {_format_number(total)}")
    print(f"Average: {_format_average(avg)}")
    print(f"Maximum: {_format_number(maximum)}")
    print(f"Minimum: {_format_number(minimum)}")


if __name__ == "__main__":
    main()


