import numpy as np

with open("input.txt", "r") as f:
    A = [list(map(int, line.split())) for line in f if line.strip()]

A = np.array(A)
N = A.shape[0]

if A.shape[0] != A.shape[1]:
    raise ValueError("Матрица должна быть квадратной!")

K = int(input("Введите K: "))

print("Матрица A:")
print(A)

F = A.copy()

mid = N // 2

if N % 2 == 0:
    r1, r2 = 0, mid
    r3, r4 = mid, N
    c1, c2 = 0, mid
    c3, c4 = mid, N
else:
    r1, r2 = 0, mid
    r3, r4 = mid + 1, N
    c1, c2 = 0, mid
    c3, c4 = mid + 1, N

area1 = F[r1:r2, c1:c2].copy()
area2 = F[r1:r2, c3:c4].copy()
area3 = F[r3:r4, c1:c2].copy()
area4 = F[r3:r4, c3:c4].copy()

count_pos_2 = 0
for i in range(area2.shape[0]):
    for j in range(area2.shape[1]):
        if j % 2 == 1 and area2[i, j] > 0:
            count_pos_2 += 1

count_neg_4 = 0
for i in range(area4.shape[0]):
    for j in range(area4.shape[1]):
        if j % 2 == 0 and area4[i, j] < 0:
            count_neg_4 += 1

print("Положительных (обл 2):", count_pos_2)
print("Отрицательных (обл 4):", count_neg_4)

if count_pos_2 > count_neg_4:
    print("Меняем области 1 и 2 симметрично")
    F[r1:r2, c1:c2] = np.fliplr(area2)
    F[r1:r2, c3:c4] = np.fliplr(area1)
else:
    print("Меняем области 3 и 4 несимметрично")
    F[r3:r4, c1:c2] = area4
    F[r3:r4, c3:c4] = area3

print("Матрица F:")
print(F)

AT = A.T

print("A^T:")
print(AT)

result = (F + A) @ AT - K * F

print("Результат (F + A) * A^T - K * F:")
print(result)
