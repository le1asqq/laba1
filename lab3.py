""" Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество нулевых  элементов в четных столбцах в области 1, 
""" то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично. 
""" При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT) . Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

 Вводим два числа K и N
K = int(input("Введите число K: "))
N = int(input("Введите число N: "))


 Формируем матрицу А
A = [[random.randint(-10, 10) for j in range(N)] for i in range(N)]


Формируем матрицы B, C, D, E
B = [[2 for j in range(N//2)] for i in range(N//2)]
C = [[0, 0, 0, 0] for i in range(N//2)] + [[1, 3, 0, 0] for i in range(N//2, N)]
D = [[4, 0, 0, 0] for i in range(N//2)] + [[0, 0, 0, 0] for i in range(N//2, N)]
E = [[2 for j in range(N//2, N)] for i in range(N//2, N)]


 Выводим матрицы B, C, D, E
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


if count_zeros > count_positives: 
    for i in range(N//2): 
        for j in range(N//2): 
            B[i][j], B[j][i] = B[j][i], B[i][j] 


  count_zero_in_4 = 0
    for i in range(len(С)//2,len(С)):
        for j in range(len(С)-(i+1)+1,i,3):
            if С [i][j] == 0:
                count_zero_in_4 += 1


    count_zeros_in_1 = 0
    for i in range(len(С)//2):
        for j in range(0,i,2):
            if С [i][j] == 0:
                count_zeros_in_1 += 1
    for i in range(len(С)//2,len(С)):
        for j in range(0,len(С)-(i+1),2):
            if С [i][j] == 0:
                count_zeros_in_1 += 1

count_zeros_in_4 > count_zeros_in_1
    for i in range(N//2):
        for j in range(N//2):
            B[i][j], B[j][i] = B[j][i], B[i][j]
else:
    C, E = E, C


 Выводим матрицу F
print("Матрица F:")
for row in C:
    print(row)


 Вычисляем выражение ((К*F)*А– (K * A^T))
esult = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):

        for k in range(N//2):   Исправление: использование правильной размерности
            result[i][j] += K * C[i][k] * A[k][j]

s_above_main = 0
for i in range(n):
    for j in range(i, n):
        if j >= i:
            s_above_main += a[i][j]
print("Сумма элементов выше главной диагонали:", s_above_main)

Сумма в области 4
 count = 0
for i in range(len(C)//2,len(C)): 
        for j in range(len(C)-(i+1)+1,i,3): 
            if C [i][j] == 0: 
                count += 1



 Сумма элементов в области 1

 count = 0
for i in range(len(C)//2): 
        for j in range(0,i,2): 
            if C [i][j] == 0: 
                count += 1 
    for i in range(len(C)//2,len(C)): 
        for j in range(0,len(C)-(i+1),2): 
            if C [i][j] == 0: 
                count += 1




Выводим результат
print("Результат:")
for row in result:
    print(row)
