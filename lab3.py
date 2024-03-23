import random

# Вводим два числа K и N
K = int(input("Введите число K: "))
N = int(input("Введите число N: "))

# Формируем матрицу А
A = [[random.randint(-10, 10) for j in range(N)] for i in range(N)]

# Формируем матрицы B, C, D, E
B = [[2 for j in range(N//2)] for i in range(N//2)]
C = [[0, 0, 0, 0] for i in range(N//2)] + [[1, 3, 0, 0] for i in range(N//2, N)]
D = [[4, 0, 0, 0] for i in range(N//2)] + [[0, 0, 0, 0] for i in range(N//2, N)]
E = [[2 for j in range(N//2, N)] for i in range(N//2, N)]

# Выводим матрицы B, C, D, E
print("Матрица B:")
for row in B:
    print(row)

print("Матрица C:")
for row in C:
    print(row)

print("Матрица D:")
for row in D:
    print(row)

print("Матрица E:")
for row in E:
    print(row)

# Формируем матрицу F
count_zeros = 0
count_positives = 0

for i in range(N//2):
    if all(elem == 0 for elem in C[i]):
        count_zeros += 1

for i in range(N//2, N, 2):
    for j in range(N//2):
        if C[i][j] > 0:
            count_positives += C[i][j]

if count_zeros > count_positives:
    for i in range(N//2):
        for j in range(N//2):
            B[i][j], B[j][i] = B[j][i], B[i][j]
else:
    C, E = E, C

# Выводим матрицу F
print("Матрица F:")
for row in C:
    print(row)

# Вычисляем выражение ((К*F)*А– (K * A^T))
result = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            result[i][j] += K * C[i][k] * A[k][j]

for i in range(N):
    for j in range(N):
        result[i][j] -= K * A[j][i]

# Выводим результат
print("Результат:")
for row in result:
    print(row)

# Считаем суммы в разных областях матрицы А
sum_below_main = 0
sum_above_main = 0
sum_area1 = 0

for i in range(N):
    for j in range(i):
        if j < i and j < N//2:
            sum_below_main += A[i][j]

for i in range(N):
    for j in range(i, N):
        if j >= i and j >= N//2:
            sum_above_main += A[i][j]

for i in range(N//2):
    for j in range(i):
        if j < i:
            sum_area1 += A[i][j]

for i in range(N//2, N):
    for j in range(N-(i+1)):
        if j < N//2:
            sum_area1 += A[i][j]

# Выводим суммы в разных областях матрицы А
print("Сумма элементов ниже главной диагонали:", sum_below_main)
print("Сумма элементов выше главной диагонали:", sum_above_main)
print("Сумма элементов в области 1:", sum_area1)
