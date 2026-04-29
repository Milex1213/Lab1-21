with open("input.txt", "r", encoding="utf-8-sig") as f:
    A = [list(map(int, line.split())) for line in f if line.strip()]

N = len(A)

if any(len(row) != N for row in A):
    raise ValueError("Матрица должна быть квадратной!")

K = int(input("Введите K: "))

print("Матрица A:")
for row in A:
    print(row)

F = [row[:] for row in A]

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

def get_area(M, r1, r2, c1, c2):
    return [row[c1:c2] for row in M[r1:r2]]

area1 = get_area(F, r1, r2, c1, c2)
area2 = get_area(F, r1, r2, c3, c4)
area3 = get_area(F, r3, r4, c1, c2)
area4 = get_area(F, r3, r4, c3, c4)

count_pos_2 = 0
for i in range(len(area2)):
    for j in range(len(area2[0])):
        if j % 2 == 1 and area2[i][j] > 0:
            count_pos_2 += 1

count_neg_4 = 0
for i in range(len(area4)):
    for j in range(len(area4[0])):
        if j % 2 == 0 and area4[i][j] < 0:
            count_neg_4 += 1

print("Положительных (обл 2):", count_pos_2)
print("Отрицательных (обл 4):", count_neg_4)

def flip_lr(matrix):
    return [row[::-1] for row in matrix]

def insert_area(M, area, r1, c1):
    for i in range(len(area)):
        for j in range(len(area[0])):
            M[r1 + i][c1 + j] = area[i][j]

if count_pos_2 > count_neg_4:
    print("Меняем области 1 и 2 симметрично")
    insert_area(F, flip_lr(area2), r1, c1)
    insert_area(F, flip_lr(area1), r1, c3)
else:
    print("Меняем области 3 и 4 несимметрично")
    insert_area(F, area4, r3, c1)
    insert_area(F, area3, r3, c3)

print("Матрица F:")
for row in F:
    print(row)

def transpose(M):
    return [list(row) for row in zip(*M)]

AT = transpose(A)

print("A^T:")
for row in AT:
    print(row)

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def multiply(A, B):
    N = len(A)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
    return result

def mul_scalar(M, k):
    return [[M[i][j] * k for j in range(len(M))] for i in range(len(M))]

def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

sum_FA = add_matrix(F, A)
print("(F + A):")
for row in sum_FA:
    print(row)

mult = multiply(sum_FA, AT)
print("(F + A) * A^T:")
for row in mult:
    print(row)

KF = mul_scalar(F, K)
print("K * F:")
for row in KF:
    print(row)

result = subtract(mult, KF)
print("Результат:")
for row in result:
    print(row)
