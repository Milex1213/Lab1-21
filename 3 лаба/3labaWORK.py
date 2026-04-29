import numpy as np

def print_matrix(name, M):
    print(f"\n{name}:")
    for row in M:
        print(" ".join(f"{x:4}" for x in row))

def generate_matrix(N):
    A = np.zeros((N, N), dtype=int)
    val = -10
    for i in range(N):
        for j in range(N):
            A[i][j] = val
            val += 1
            if val > 10:
                val = -10
    return A

def count_elements(A, mid):
    area2 = A[:mid, mid:]
    area4 = A[mid:, mid:]

    pos = 0
    for j in range(area2.shape[1]):
        if (j + 1) % 2 == 0:  # четные столбцы (1-based)
            pos += np.sum(area2[:, j] > 0)

    neg = 0
    for j in range(area4.shape[1]):
        if (j + 1) % 2 == 1:  # нечетные столбцы (1-based)
            neg += np.sum(area4[:, j] < 0)

    return pos, neg

def build_F(A):
    N = A.shape[0]
    mid = N // 2
    F = A.copy()

    pos, neg = count_elements(A, mid)

    print(f"\nПоложительных в области 2 (четные столбцы): {pos}")
    print(f"Отрицательных в области 4 (нечетные столбцы): {neg}")

    if pos > neg:
        a1 = A[:mid, :mid].copy()
        a2 = A[:mid, mid:].copy()
        F[:mid, :mid] = np.fliplr(a2)
        F[:mid, mid:] = np.fliplr(a1)
    else:
        a3 = A[mid:, :mid].copy()
        a4 = A[mid:, mid:].copy()
        F[mid:, :mid] = a4
        F[mid:, mid:] = a3

    return F

def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    A = generate_matrix(N)
    print_matrix("Матрица A", A)

    F = build_F(A)
    print_matrix("Матрица F", F)

    AT = A.T
    print_matrix("A^T", AT)

    FA = F + A
    print_matrix("F + A", FA)

    result = np.dot(FA, AT) - K * F
    print_matrix("(F + A) * A^T - K * F", result)

if __name__ == "__main__":
    main()
