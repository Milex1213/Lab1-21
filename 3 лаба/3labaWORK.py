import numpy as np

K = int(input("Введите K: "))

with open("matrix.txt", "r") as f:
    N = int(f.readline())
    A = [list(map(int, f.readline().split())) for _ in range(N)]

A = np.array(A)

print("\nМатрица A:")
print(A)

F = A.copy()

mid = N // 2

area1 = (slice(None), slice(0, mid))
area2 = (slice(0, mid), slice(None))
area3 = (slice(None), slice(mid, N))
area41 = (slice(mid, N), slice(None))

count_pos = 0
for i in range(0, mid):
    for j in range(N):
        if j % 2 == 0 and A[i][j] > 0:
            count_pos += 1

count_neg = 0
for i in range(mid, N):
    for j in range(N):
        if j % 2 != 0 and A[i][j] < 0:
            count_neg += 1

print("\nПоложительных:", count_pos)
print("Отрицательных:", count_neg)

if count_pos > count_neg:
    temp = F[area1].copy()
    F[area1] = F[area2].T
    F[area2] = temp.T
else:
    temp = F[area3].copy()
    F[area3] = F[area41]
    F[area41] = temp

print("\nМатрица F:")
print(F)

sum_FA = F + A
print("\nF + A:")
print(sum_FA)

AT = A.T
print("\nA^T:")
print(AT)

mult = np.dot(sum_FA, AT)
print("\n(F + A) * A^T:")
print(mult)

KF = K * F
print("\nK * F:")
print(KF)

result = mult - KF
print("\nРезультат:")
print(result)
