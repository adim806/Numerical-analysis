import numpy as np


def calculation(right, left, xf):
    return ((xf * ((right[1] - left[1]) / (right[0] - left[0]))) +
            ((left[1] * right[0] - right[1] * left[0]) / (right[0] - left[0])))


def linearInter(poit_list, x):
    left = (-10000000000, 0)
    right = (10000000000, 0)
    for point in poit_list[1:]:
        if left[0] < point[0] < x:
            left = point
        if right[0] > point[0] > x:
            right = point
    return calculation(right, left, x)


def polynomialInter(vec_x, x):
    return vec_x[0] + vec_x[1] * x + vec_x[2] * (x ** 2)


def vectorX(pl):
    matrix = np.array([[1, pl[0][0], pl[0][0] ** 2],
                       [1, pl[1][0], pl[1][0] ** 2],
                       [1, pl[2][0], pl[2][0] ** 2]])

    vecB = np.array([pl[0][1], pl[1][1], pl[2][1]])
    solution = np.linalg.solve(matrix, vecB)
    return solution


def lagrange_interpolation(x_values, y_values):
    def L(i, x):
        result = 1
        for j in range(len(x_values)):
            if j != i:
                result *= (x - x_values[j]) / (x_values[i] - x_values[j])
        return result

    def P(x):
        result = 0
        for i in range(len(x_values)):
            result += y_values[i] * L(i, x)
        return result

    return P


def main():
    while True:
        choice = int(input(
            "Choose the option you want: \n"
            "1 - Linear Interpolation\n"
            "2 - Polynomial Interpolation\n"
            "3 - Lagrange Interpolation\n"
            "4 - Exit\n"))
        match choice:
            case 1:
                pointList1 = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
                x1 = 2.5
                print("Y: %.4f" % linearInter(pointList1, x1), f" Estimate for {x1}\n")
            case 2:
                x2 = 2.5
                pointList2 = [(1, 0.8415), (2, 0.9093), (3, 0.1411)]
                print("Y:", round(polynomialInter(vectorX(pointList2)), x2), f" Estimate for {x2}\n")
            case 3:
                x_values = [1, 2, 4]
                y_values = [1, 0, 1.5]
                x3 = 3
                interpolating_polynomial = lagrange_interpolation(x_values, y_values)
                print(f"P({x3}) = {interpolating_polynomial(x3):.4f} Estimate for {x3}\n")
            case 4:
                break


if __name__ == "__main__":
    main()
