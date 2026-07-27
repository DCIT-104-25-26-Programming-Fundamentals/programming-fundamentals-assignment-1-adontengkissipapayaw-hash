# =============================================================================
# Fibonacci Sequence — Friendly Generator
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series where each number is the sum of the
# two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# This program has two fun parts:
# A) Print the first N terms of the Fibonacci sequence
# B) Check whether a number you pick is in the Fibonacci sequence
#
# Both parts use loops (not recursion) to generate the sequence.
#
# =============================================================================
# YOUR CODE BELOW — implement the required functions
# =============================================================================


def get_fibonacci_sequence(n):
    """Generate and return the first n Fibonacci numbers as a list."""
    if n <= 0:
        return []
    
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def part_a():
    """Part A: Print the first N terms of Fibonacci sequence."""
    print("\n" + "=" * 50)
    print("PART A: First N Fibonacci Numbers")
    print("=" * 50)
    
    try:
        n = int(input("\nHow many terms would you like? "))
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return
        
        sequence = get_fibonacci_sequence(n)
        terms_str = " ".join(str(num) for num in sequence)
        print(f"\nFibonacci sequence ({n} terms): {terms_str}")
    except ValueError:
        print("Error: Please enter a valid positive integer.")


def is_fibonacci_number(num):
    """Check if a number is in the Fibonacci sequence."""
    if num < 0:
        return False
    
    # Generate Fibonacci numbers until we reach or exceed num
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    return a == num


def part_b():
    """Part B: Check if a number is a Fibonacci number."""
    print("\n" + "=" * 50)
    print("PART B: Is It a Fibonacci Number?")
    print("=" * 50)
    
    try:
        num = int(input("\nEnter a number to check: "))
        if num < 0:
            print("Error: Please enter a non-negative integer.")
            return
        
        if is_fibonacci_number(num):
            print(f"\n✓ {num} is a Fibonacci number!")
        else:
            print(f"\n✗ {num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Please enter a valid integer.")


def main():
    """Main menu to choose an operation."""
    print("\nFibonacci Sequence Generator")
    print("───────────────────────────")
    print("\nChoose an operation:")
    print("  A  Print first N Fibonacci numbers")
    print("  B  Check if a number is Fibonacci")
    print("  Q  Quit")
    
    choice = input("\nEnter your choice (A/B/Q): ").upper()
    
    if choice == 'A':
        part_a()
    elif choice == 'B':
        part_b()
    elif choice == 'Q':
        print("\nGoodbye!")
    else:
        print("\nError: Please enter A, B, or Q.")


if __name__ == "__main__":
    main()

