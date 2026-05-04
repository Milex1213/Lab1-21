K = int(input("Введите K: "))

with open("matrix.txt", "r") as f:
    A = [list(map(int, line.split())) for line in f if line.strip()]

N = len(A)

print("\nМатрица A:")
for row in A:
    print(row)

F = [row[:] for row in A]

mid = N // 2

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

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

if count_pos > count_neg:
    print("\nСимметричный обмен областей 1 и 2")

    area1 = [row[:mid] for row in F]
    area2 = F[:mid]

    area1_T = transpose(area1)
    area2_T = transpose(area2)

    for i in range(N):
        for j in range(mid):
            F[i][j] = area2_T[i][j]

    for i in range(mid):
        for j in range(N):
            F[i][j] = area1_T[i][j]

else:
    print("\nНесимметричный обмен областей 3 и 4")

    area3 = [row[mid:] for row in F]
    area4 = F[mid:]

    for i in range(N):
        for j in range(mid):
            if i >= mid:
                F[i][j + mid] = area4[i - mid][j]

    for i in range(mid):
        for j in range(N):
            if j < len(area3[i]):
                F[i + mid][j] = area3[i][j]

print("\nМатрица F:")
for row in F:
    print(row)

sum_FA = [[A[i][j] + F[i][j] for j in range(N)] for i in range(N)]

print("\nF + A:")
for row in sum_FA:
    print(row)

AT = transpose(A)

print("\nA^T:")
for row in AT:
    print(row)

def multiply(A, B):
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

mult = multiply(sum_FA, AT)

print("\n(F + A) * A^T:")
for row in mult:
    print(row)

KF = [[K * F[i][j] for j in range(N)] for i in range(N)]

print("\nK * F:")
for row in KF:
    print(row)

result = [[mult[i][j] - KF[i][j] for j in range(N)] for i in range(N)]

print("\nРезультат:")
for row in result:
    print(row)
