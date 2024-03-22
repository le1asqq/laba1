import random

# Ввод данных с клавиатуры
K = int(input("Введите K: "))
N = int(input("Введите N: "))

# Инициализация матрицы A(N,N)
A = [[0 for _ in range(N)] for _ in range(N)]

# Заполнение подматриц B, C, D, E
for i in range(N):
    for j in range(N):
        if i < N/2:
            if j < N/2:
                A[i][j] = random.randint(-10, 10)  # заполнение подматрицы B
            else:
                A[i][j] = random.randint(-10, 10)  # заполнение подматрицы C
        else:
            if j < N/2:
                A[i][j] = random.randint(-10, 10)  # заполнение подматрицы D
            else:
                A[i][j] = random.randint(-10, 10)  # заполнение подматрицы E

# Функция для вычисления количества нулевых элементов в области 4
def count_zeros_in_area_4(matrix):
    count = 0
    for i in range(N//2 + N % 2, N):
        for j in range(N//2):
            if matrix[i][j] == 0:
                count += 1
    return count

# Функция для вычисления количества нулевых элементов в области 1
def count_zeros_in_area_1(matrix):
    count = 0
    for i in range(N//2):
        for j in range(i):
            if matrix[i][j] == 0:
                count += 1
    for i in range(N//2, N):
        for j in range(N-(i+1)):
            if matrix[i][j] == 0:
                count += 1
    return count

# Формирование матрицы F в зависимости от условия
if count_zeros_in_area_4(A) > count_zeros_in_area_1(A):
    # Поменять в В симметрично области 2 и 3 местами
    for i in range(N//2):
        for j in range(N//2, N):
            A[i][j], A[N-i-1][j] = A[N-i-1][j], A[i][j]
else:
    # Поменять С и E местами несимметрично
    for i in range(N//2 + N % 2):
        for j in range(N//2):
            A[i][j], A[N-i-1][N-j-1] = A[N-i-1][N-j-1], A[i][j]

# Вывод матрицы A
print("Матрица A:")
for row in A:
    print(' '.join([str(elem) for elem in row]))

# Вычисление выражения ((F*A)– (K * AT))
result = [[0 for _ in range(N)] for _ in range(N)]
AT = [[A[j][i] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            result[i][j] += A[i][k] * A[k][j]
        result[i][j] -= K * AT[i][j]

# Вывод результата
print("Результат выражения ((F*A)– (K * AT)):")
for row in result:
    print(' '.join([str(elem) for elem in row]))
