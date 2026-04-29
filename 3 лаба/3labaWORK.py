import numpy as np

# ---------- Чтение матрицы из файла ----------
with open("input.txt", "r") as f:
    A = [list(map(int, line.split())) for line in f if line.strip()]

A = np.array(A)
N = A.shape[0]

# Проверка, что матрица квадратная
if A.shape[0] != A.shape[1]:
    raise ValueError("Матрица должна быть квадратной!")

# ---------- Ввод K ----------
K = int(input("Введите K: "))

print("Матрица A:")
print(A)

# ---------- Формирование F ----------
F = A.copy()
half = N // 2

# Области
area1 = F[:half, :half].copy()
area2 = F[:half, half:].copy()
area3 = F[half:, :half].copy()
area4 = F[half:, half:].copy()

# ---------- Подсчёты ----------
count_pos_2 = 0
for i in range(area2.shape[0]):
    for j in range(area2.shape[1]):
        if j % 2 == 1 and area2[i, j] > 0:  # чётные столбцы
            count_pos_2 += 1

count_neg_4 = 0
for i in range(area4.shape[0]):
    for j in range(area4.shape[1]):
        if j % 2 == 0 and area4[i, j] < 0:  # нечётные столбцы
            count_neg_4 += 1

print("Положительных (обл 2, четн столбцы):", count_pos_2)
print("Отрицательных (обл 4, нечетн столбцы):", count_neg_4)

# ---------- Условие ----------
if count_pos_2 > count_neg_4:
    print("Меняем области 1 и 2 симметрично")

    F[:half, :half] = np.fliplr(area2)
    F[:half, half:] = np.fliplr(area1)

else:
    print("Меняем области 3 и 4 несимметрично")

    F[half:, :half] = area4
    F[half:, half:] = area3

print("Матрица F:")
print(F)

# ---------- Матричные операции ----------
AT = A.T

print("A^T:")
print(AT)

result = (F + A) @ AT - K * F

print("Результат (F + A) * A^T - K * F:")
print(result)
