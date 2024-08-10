import copy


matrix = [[2, 1, 0],
          [1, 3, -1],
          [0, 1, 2]]

vector = [6, 0, 3]
tolerance = 0.001


def has_strong_diagonal(mat):
    """Checks for strong diagonal dominance in the matrix."""
    for i in range(len(mat)):
        row_sum = sum(abs(mat[i][j]) for j in range(len(mat)) if i != j)
        if abs(mat[i][i]) <= row_sum:
            return False
    return True


def decompose_matrix(mat):
    """Decomposes matrix into diagonal and non-diagonal components."""
    diag_matrix = [[0] * len(mat) for _ in range(len(mat))]
    non_diag_matrix = copy.deepcopy(mat)
    for i in range(len(mat)):
        diag_matrix[i][i] = mat[i][i]
        non_diag_matrix[i][i] = 0
    return diag_matrix, non_diag_matrix


def initialize_vector(length):
    """Initializes a zero vector of the given length."""
    return [0] * length


def is_solution_valid(current, next):
    """Checks if the solution has converged based on the tolerance."""
    return all(abs(next[i] - current[i]) <= tolerance for i in range(len(current)))


def jacobi_method(mat, vec):
    """Solves linear equations using the Jacobi method."""
    if not has_strong_diagonal(mat):
        return "Matrix does not have strong diagonal"

    def calculate_next_guess(diag, non_diag, guess, next_guess):
        """Computes the next guess for Jacobi."""
        for i in range(len(guess)):
            row_sum = sum(non_diag[i][j] * guess[j] for j in range(len(guess)))
            next_guess[i] = (vec[i] - row_sum) / diag[i][i]
        print(next_guess)

    return find_solution(mat, calculate_next_guess)


def gauss_seidel_method(mat, vec):
    """Solves linear equations using the Gauss-Seidel method."""
    if not has_strong_diagonal(mat):
        return "Matrix does not have strong diagonal"

    def calculate_next_guess(diag, non_diag, guess, next_guess):
        """Computes the next guess for Gauss-Seidel."""
        for i in range(len(guess)):
            for j in range(len(guess)):
                if i > j:
                    guess[i - 1] = next_guess[i - 1]
                row_sum = sum(non_diag[i][j] * guess[j] for j in range(len(guess)))
                next_guess[i] = (vec[i] - row_sum) / diag[i][i]
                break
        print(next_guess)

    return find_solution(mat, calculate_next_guess)


def find_solution(mat, calculate_next_guess):
    """Finds the solution vector using an iterative method."""
    iterations = 1
    current_guess = initialize_vector(len(mat))
    next_guess = initialize_vector(len(mat))
    diag_matrix, non_diag_matrix = decompose_matrix(mat)

    calculate_next_guess(diag_matrix, non_diag_matrix, current_guess, next_guess)

    while not is_solution_valid(current_guess, next_guess):
        iterations += 1
        current_guess = next_guess.copy()
        calculate_next_guess(diag_matrix, non_diag_matrix, current_guess, next_guess)

    return f'Iterations: {iterations}, \tSolution: {next_guess}'


def main():
    """Runs Jacobi and Gauss-Seidel methods and prints results."""
    print("Matrix:", matrix)
    print("\nSolution Vector:", vector)
    print("\nJacobi method for solving linear equations:")
    print(jacobi_method(matrix, vector))
    print("\nGauss-Seidel method for solving linear equations:")
    print(gauss_seidel_method(matrix, vector))


if __name__ == "__main__":
    main()
