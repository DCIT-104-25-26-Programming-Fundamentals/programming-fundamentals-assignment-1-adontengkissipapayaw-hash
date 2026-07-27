# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols):
    """Read a matrix of size rows x cols from the user."""
    matrix = []
    for i in range(1, rows + 1):
        while True:
            try:
                row_input = input(f"Enter row {i}: ")
                values = row_input.split()
                if len(values) != cols:
                    print(f"Error: Please enter exactly {cols} values.")
                    continue
                row = [float(v) for v in values]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
    return matrix


def display_matrix(matrix, name="Matrix"):
    """Display a matrix in neat, aligned grid format."""
    if not matrix:
        print(f"{name}: (empty)")
        return
    
    print(f"\n{name}:")
    # Find the maximum width needed for any element
    max_width = 0
    for row in matrix:
        for val in row:
            # Format as int if whole, else as float
            if isinstance(val, float) and val.is_integer():
                s = str(int(val))
            else:
                s = str(round(val, 2))
            max_width = max(max_width, len(s))
    
    # Print rows aligned
    for row in matrix:
        formatted_row = []
        for val in row:
            if isinstance(val, float) and val.is_integer():
                s = str(int(val))
            else:
                s = str(round(val, 2))
            formatted_row.append(s.rjust(max_width))
        print("  " + "  ".join(formatted_row))


def transpose(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Add two matrices element-wise."""
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiply two matrices: A (m x n) × B (n x p) = C (m x p)."""
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])
    
    # Check if multiplication is valid
    if n != len(matrix_b):
        return None
    
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            value = 0
            for k in range(n):
                value += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(value)
        result.append(new_row)
    return result


def part_a():
    """Part A: Transpose a matrix."""
    print("\n" + "=" * 50)
    print("PART A: Transpose a Matrix")
    print("=" * 50)
    try:
        m = int(input("How many rows? "))
        n = int(input("How many columns? "))
        if m <= 0 or n <= 0:
            print("Error: rows and columns must be positive integers.")
            return
        print(f"Enter the {m} × {n} matrix (one row per line):")
        matrix = read_matrix(m, n)
        transposed = transpose(matrix)
        display_matrix(matrix, "Original Matrix")
        display_matrix(transposed, "Transposed Matrix")
    except ValueError:
        print("Error: Please enter valid integers.")


def part_b():
    """Part B: Add two matrices."""
    print("\n" + "=" * 50)
    print("PART B: Add Two Matrices")
    print("=" * 50)
    try:
        m = int(input("How many rows? "))
        n = int(input("How many columns? "))
        if m <= 0 or n <= 0:
            print("Error: rows and columns must be positive integers.")
            return
        print(f"Enter the first {m} × {n} matrix:")
        matrix_a = read_matrix(m, n)
        print(f"Enter the second {m} × {n} matrix:")
        matrix_b = read_matrix(m, n)
        result = add_matrices(matrix_a, matrix_b)
        if result is None:
            print("Error: matrices must be the same size.")
            return
        display_matrix(matrix_a, "Matrix A")
        display_matrix(matrix_b, "Matrix B")
        display_matrix(result, "A + B (Result)")
    except ValueError:
        print("Error: Please enter valid integers.")


def part_c():
    """Part C: Multiply two matrices."""
    print("\n" + "=" * 50)
    print("PART C: Multiply Two Matrices")
    print("=" * 50)
    try:
        m = int(input("Rows in matrix A? "))
        n = int(input("Columns in matrix A (= rows in matrix B)? "))
        p = int(input("Columns in matrix B? "))
        if m <= 0 or n <= 0 or p <= 0:
            print("Error: all dimensions must be positive integers.")
            return
        print(f"Enter matrix A ({m} × {n}):")
        matrix_a = read_matrix(m, n)
        print(f"Enter matrix B ({n} × {p}):")
        matrix_b = read_matrix(n, p)
        result = multiply_matrices(matrix_a, matrix_b)
        if result is None:
            print("Error: incompatible matrix dimensions for multiplication.")
            return
        display_matrix(matrix_a, "Matrix A")
        display_matrix(matrix_b, "Matrix B")
        display_matrix(result, "A × B (Result)")
    except ValueError:
        print("Error: Please enter valid integers.")


def main():
    """Main menu to choose an operation."""
    print("\nMatrix Operations Calculator")
    print("────────────────────────────")
    print("Choose an operation:")
    print("  A  Transpose a matrix")
    print("  B  Add two matrices")
    print("  C  Multiply two matrices")
    print("  Q  Quit")
    
    choice = input("\nEnter your choice (A/B/C/Q): ").upper()
    
    if choice == 'A':
        part_a()
    elif choice == 'B':
        part_b()
    elif choice == 'C':
        part_c()
    elif choice == 'Q':
        print("Goodbye!")
    else:
        print("Error: Please enter A, B, C, or Q.")


if __name__ == "__main__":
    main()

