
size = 3
I = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

input_mat = [[1, -1, -2],
             [2, -3, -5],
             [-1, 3, 5]]

input_vector = [1, 2, 3]


def mat_mult(mat_a, mat_b):  # matrix multiplication function, returns result of mat_a * mat_b
    rows_a, cols_a = len(mat_a), len(mat_a[0])
    rows_b, cols_b = len(mat_b), len(mat_b[0])

    if cols_a != rows_b:
        raise ValueError("Matrices cannot be multiplied due to incompatible dimensions.")

    res = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                res[i][j] += mat_a[i][k] * mat_b[k][j]

    return res


def get_inverse(mat):  # returns the inverse of the matrix
    n = len(mat)
    inverse = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def prep_lead(mat, inverse, index):  # making the pivot element 1
        try:
            coeff = 1 / mat[index][index]
        except ZeroDivisionError:
            raise ValueError("The given matrix does not have an inverse.")

        mat[index] = [elem * coeff for elem in mat[index]]
        inverse[index] = [elem * coeff for elem in inverse[index]]
        return mat, inverse

    def reduce_column(mat, inverse, index):  # reducing the column to echelon form
        for i in range(len(mat)):
            if i == index:
                continue
            coeff = -mat[i][index]
            mat[i] = [x + coeff * y for x, y in zip(mat[i], mat[index])]
            inverse[i] = [x + coeff * y for x, y in zip(inverse[i], inverse[index])]
        return mat, inverse

    for i in range(n):
        mat, inverse = prep_lead(mat, inverse, i)
        mat, inverse = reduce_column(mat, inverse, i)

    return inverse


def get_norm(mat):  # returns the norm of the matrix
    return max(sum(abs(mat[i][j]) for j in range(len(mat))) for i in range(len(mat)))


def lu_decomposition(mat):  # performs LU decomposition
    n = len(mat)
    lower = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    upper = [row[:] for row in mat]

    for j in range(n):
        for i in range(j + 1, n):
            factor = upper[i][j] / upper[j][j]
            lower[i][j] = factor
            for k in range(j, n):
                upper[i][k] -= factor * upper[j][k]

    return lower, upper


def forward_substitution(lower, b):  # forward substitution to solve Ly = b
    n = len(lower)
    y = [0] * n
    for i in range(n):
        y[i] = b[i] - sum(lower[i][j] * y[j] for j in range(i))
    return y


def backward_substitution(upper, y):  # backward substitution to solve Ux = y
    n = len(upper)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(upper[i][j] * x[j] for j in range(i + 1, n))) / upper[i][i]
    return x


def solve_lu_decomposition(mat, b):
    lower, upper = lu_decomposition(mat)
    y = forward_substitution(lower, b)
    return backward_substitution(upper, y)


def main():
    print("\nInput matrix:")
    for row in input_mat:
        print(row)

    try:
        inverse = get_inverse([row[:] for row in input_mat])
        print("\nInverse matrix:")
        for row in inverse:
            print(row)
    except ValueError as e:
        print(e)
        return

    print("\nInput vector:")
    print(input_vector)

    mat_copy = [row[:] for row in input_mat]
    solution = solve_lu_decomposition(mat_copy, input_vector)

    print("\nSolution vector:")
    print(solution)


if __name__ == "__main__":
    main()
