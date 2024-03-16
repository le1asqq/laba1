#Формируется матрица F след.образом:если в С кол-во нулевых элементов в четных столбцах в области 1,то поменять в В симметрично области 2 и 3 местами,иначе С и Е поменять местами несиметрично.
При этом матрица вычисляется выражение ((F*A)-(K*AT).Выводятся по мере формирования А,F и все матричные операции последовательно.#

import random

# Функция для генерации квадратной матрицы размера N x N с случайными числами в диапазоне [-10, 10]
def generate_matrix(N):
    matrix = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix


# Функция для вывода матрицы
def print_matrix(matrix):
    for row in matrix:
        print(row)


# Функция для получения подматрицы из матрицы
def get_submatrix(matrix, start_row, start_col, size):
    submatrix = []
    for i in range(start_row, start_row + size):
        submatrix.append(matrix[i][start_col:start_col + size])
    return submatrix


# Функция для подсчета количества нулей в определенной области матрицы
def count_zeroes(matrix, start_row, start_col, size, is_odd):
    count = 0
    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            if is_odd:
                if j % 2 != 0 and matrix[i][j] == 0:
                    count += 1
            else:
                if j % 2 == 0 and matrix[i][j] == 0:
                    count += 1
    return count


# Функция для обмена двух подматриц местами
def swap_submatrices(matrix, submatrix1, submatrix2, start_row, start_col, size):
    for i in range(size):
        for j in range(size):
            matrix[start_row + i][start_col + j], matrix[submatrix1[0] + i][submatrix1[1] + j] = \
                matrix[submatrix1[0] + i][submatrix1[1] + j], matrix[start_row + i][start_col + j]
            matrix[start_row + i][start_col + j], matrix[submatrix2[0] + i][submatrix2[1] + j] = \
                matrix[submatrix2[0] + i][submatrix2[1] + j], matrix[start_row + i][start_col + j]


# Функция для формирования матрицы F
def calculate_F(matrix, K):
    B = get_submatrix(matrix, 0, 0, 2)
    C = get_submatrix(matrix, 0, 2, 2)
    D = get_submatrix(matrix, 2, 0, 2)
    E = get_submatrix(matrix, 2, 2, 2)

    count_zeroes_even_C = count_zeroes(matrix, 0, 2, 2, False)
    count_zeroes_odd_C = count_zeroes(matrix, 2, 2, 2, True)

    # Проверяем условие и меняем подматрицы местами в соответствии с ним
    if count_zeroes_odd_C > count_zeroes_even_C:
        swap_submatrices(matrix, (0, 0), (2, 2), 0, 2, 2)
    else:
        swap_submatrices(matrix, (0, 2), (2, 2), 0, 0, 2)


# Функция для транспонирования матрицы
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# Функция для умножения двух матриц
def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result


# Основная функция программы
def main():
    K = int(input("Enter K: "))  # Запрос числа K с клавиатуры
    N = int(input("Enter N: "))  # Запрос числа N с клавиатуры

    # Создание матрицы A с помощью функции generate_matrix
    A = generate_matrix(N)
    print("Matrix A:")
    print_matrix(A)
    print()

    # Формирование матрицы F в соответствии с условиями задачи
    calculate_F(A, K)
    print("Matrix F:")
    print_matrix(A)
    print()

    # Транспонирование матрицы A
    A_transpose = transpose_matrix(A)
    print("Transpose of Matrix A:")
    print_matrix(A_transpose)
    print()

    # Умножение матрицы A на саму себя (F * A)
    F_times_A = matrix_multiplication(A, A)
    print("F * A:")
    print_matrix(F_times_A)
    print()

    # Умножение числа K на транспонированную матрицу A
    K_times_A_transpose = [[-K * num for num in row] for row in A_transpose]
    print("K * Transpose of Matrix A:")
    print_matrix(K_times_A_transpose)
    print()

    # Вычисление конечного результата согласно условиям задачи
    result = [[F_times_A[i][j] - K_times_A_transpose[i][j] for j in range(N)] for i in range(N)]
    print("Final Result:")
    print_matrix(result)


main()
