import random
import time


def print_m(M, tt):
    print(" время = " + str(tt) + " seconds.")
    for i in M:
        for j in i:
            print("%5d" % j, end=' ')

        print()


def summatr(matrix1,matrix2): #Сложение матриц
    summa=[[0]*len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            summa[i][j]=matrix1[i][j]+matrix2[i][j]
    return summa

def diffmatr(matrix1, matrix2): #Разница матриц
    diff = [[0] * len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            diff[i][j] = matrix1[i][j] - matrix2[i][j]
    return diff

def matr_multi_matr(matrix1, matrix2): #Умножение двух матриц
    multi = [[0] * len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for u in range(len(matrix1)):
            for j in range(len(matrix1)):
                multi[i][u] += matrix1[i][j] * matrix2[j][u]
    return multi

def matr_multi_number(matrix1,K): #Умножение матрицы на число
    mdigit=[[0] * len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            mdigit[i][j] = matrix1[i][j]*K
    return mdigit

def matr_tra(matrix):
    tra = [[0] * N for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            tra[i][j] = matrix[j][i]
    return tra

N = int(input("Введите N в интервале от 6 до 100:"))
while N < 6 or N > 100:
    row_q = int(input(
        "Вы ввели неверное число"))
K = int(input("Введите число К="))
start = time.time()

A = [[0] * N for i in range(N)]  # создание матрицы A
for i in range(N):
    for j in range(N):
        A[i][j] = random.randint(-10, 10)
print("A")
time_next = time.time()
print_m(A, time_next - start)


B = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы B
for i in range(int(len(A) // 2)):
    for j in range(int((len(A)) // 2)):
        B[i][j] = A[i][j]
print("B")
time_next = time.time()
print_m(B, time_next - start)


C = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы C
for i in range(int(len(A) // 2)):
    for j in range(int((len(A) + 1) // 2), len(A)):
        C[i][j - int((N + 1) / 2)] = A[i][j]
print("C")
time_next = time.time()
print_m(C, time_next - start)


E = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы E
for i in range((int(len(A) + 1) // 2), len(A)):
    for j in range(int((len(A) + 1) // 2), len(A)):
        E[i - int((N + 1) / 2)][j - int((N + 1) / 2)] = A[i][j]
print("E")
time_next = time.time()
print_m(E, time_next - start)


D = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы D
for i in range(int(len(A) // 2), len(A)):
    for j in range(int((len(A)) // 2)):
        D[i - int((N + 1) / 2)][j] = A[i][j]
print("D")
time_next = time.time()
print_m(D, time_next - start)


F = [[0] * N for i in range(N)]  # Создание матрицы F равной A
for i in range(N):
    for j in range(N):
        F[i][j] = A[i][j]
print("F")
time_next = time.time()
print_m(F, time_next - start)


chek_1 = 0
start_p = 0
finish_p = 0
for i in range(N // 2):  # нули
    for j in range(start_p, finish_p):

        if C[i][j] == 0 and (i + j) % 2 == 0:
            chek_1 += 1

    if i == N // 2 // 2 - 1:
        pass
    else:
        if i > N // 2 // 2 - 1:

            finish_p -= 1
        else:

            finish_p += 1

# print("C")
# time_next = time.time()
# print_m(C, time_next - start)


start_p = 0
finish_p = N//2
chek_2 = 0
has_m = []
for i in range(N // 2):  # подготавливаем масив для счета периметра
    has_m.append([])
    if start_p <= N // 2 // 2 and finish_p >= N // 2 // 2:
        start_p += 1
        finish_p -= 1
    for j in range(start_p, finish_p):
        has_m[i].append(C[i][j])

# print("C")
# time_next = time.time()
# print_m(C, time_next - start)


new_has_m = [] # считаем произведение периметра
for i in has_m:
    if i != []:
        new_has_m.append(i)
for i in new_has_m[0]:
    chek_2 *= i

for i in new_has_m[-1]:
    chek_2 *= i
for i in range(1, len(new_has_m)):
    chek_2 *= new_has_m[i][0]
    chek_2 *= new_has_m[i][-1]





if chek_1 > chek_2:
    # если в С количество нулей в ячейках с четной суммой индексов в области 1 больше,
    # чем произведение чисел по периметру области 2, то поменять в С симметрично области 1 и 2 местами,
    # иначе С и В поменять местами несимметрично

    start_p = 0
    finish_p = N // 2
    chek_2 = 0

    for i in range(N // 2):  # обрабатываем подматрицу C под номером 2 и симетрично меняем на 1
        if start_p <= N // 2 // 2 and finish_p >= N // 2 // 2:
            start_p += 1
            finish_p -= 1
        for j in range(start_p, finish_p):
            C[i][j], C[j][i] = C[j][i], C[i][j]

    print("C")
    time_next = time.time()
    print_m(C, time_next - start)
else:  # если нет меняем не симетрично B и С
    for i in range(0, N // 2):
        for j in range(0, N // 2):
            F[i][j], F[i][-j -1] = F[i][-j - 1], F[i][j]
    print("F")
    time_next = time.time()
    print_m(F, time_next - start)

print("Результат:")

result=[[0]*N for i in range(N)] #Итоговая матрица
result=diffmatr(matr_multi_matr(matr_tra(A), summatr(F, A)), matr_multi_number(matr_tra(F), K)) # финальное выражение
print_m(result, time_next - start)