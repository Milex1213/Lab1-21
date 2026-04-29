import numpy as np

def print_matrix(name, M):
    print(f"\n{name}:")
    for row in M:
        print(" ".join(f"{x:4}" for x in row))


def split_matrix(A):
    n = A.shape[0]
    mid = n // 2
    
    area1 = A[:mid, :mid]
    area2 = A[:mid, mid:]
    area3 = A[mid:, :mid]
    area4 = A[mid:, mid:]
    
    return area1.copy(), area2.copy(), area3.copy(), area4.copy()


def count_condition(area2, area4):
    count_pos = 0
    for j in range(area2.shape[1]):
        if j % 2 == 1:
            count_pos += np.sum(area2[:, j] > 0)

    count_neg = 0
    for j in range(area4.shape[1]):
        if j % 2 == 0:
            count_neg += np.sum(area4[:, j] < 0)

    return count_pos, count_neg


def build_F(A):
    n = A.shape[0]
    F = A.copy()
    
    a1, a2, a3, a4 = split_matrix(A)
    
    pos, neg = count_condition(a2, a4)
    
    print(f"\nПоложительных в области 2 (четные столбцы): {pos}")
    print(f"Отрицательных в области 4 (нечетные столбцы): {neg}")
    
    mid = n // 2

    if pos > neg:
        F[:mid, :mid] = np.fliplr(a2)
        F[:mid, mid:] = np.fliplr(a1)
    else:
        F[mid:, :mid] = a4
        F[mid:, mid:] = a3

    return F


def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    print("Введите матрицу A построчно:")
    A = []
    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)

    A = np.array(A)

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
