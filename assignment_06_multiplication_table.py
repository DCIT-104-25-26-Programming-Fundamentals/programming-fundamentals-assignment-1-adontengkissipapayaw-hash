# =============================================================================
# Multiplication Table Generator — Friendly Edition
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# This program generates multiplication tables using loops and functions.
# You can view a single table for any number, or all tables from 1 to N.
#
# Features:
# - Part A: Print a single table (1 to 12) for a number you choose
# - Part B: Print all tables from 1 to N, each nicely separated
#
# =============================================================================
# YOUR CODE BELOW — implement the required functions
# =============================================================================


def print_single_table(n):
    """Print the multiplication table for n (from 1 to 12)."""
    print(f"\nMultiplication Table for {n}:")
    print("─" * 30)
    for i in range(1, 13):
        result = n * i
        print(f"  {n:3d}  ×  {i:2d}  =  {result:4d}")


def print_multiple_tables(n):
    """Print multiplication tables for all numbers from 1 to n."""
    for num in range(1, n + 1):
        print_single_table(num)
        if num < n:
            print("─" * 30)


def part_a():
    """Part A: Single multiplication table."""
    print("\n" + "=" * 50)
    print("PART A: Single Multiplication Table")
    print("=" * 50)
    
    try:
        num = int(input("\nEnter a number: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
            return
        print_single_table(num)
    except ValueError:
        print("Error: Please enter a valid positive integer.")


def part_b():
    """Part B: Multiple multiplication tables (1 to N)."""
    print("\n" + "=" * 50)
    print("PART B: Multiplication Tables from 1 to N")
    print("=" * 50)
    
    try:
        n = int(input("\nHow many tables would you like (1 to N)? "))
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return
        print_multiple_tables(n)
    except ValueError:
        print("Error: Please enter a valid positive integer.")


def main():
    """Main menu to choose an operation."""
    print("\nMultiplication Table Generator")
    print("──────────────────────────────")
    print("\nChoose an option:")
    print("  A  Print one table")
    print("  B  Print tables from 1 to N")
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

