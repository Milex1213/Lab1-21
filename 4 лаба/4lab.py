import numpy as np
import matplotlib.pyplot as plt

def get_matrix(N):
    while True:
        mode = input("Способ (1-файл, 2-случайная): ")
        if mode == "1":
            try:
                A = np.loadtxt("matrix.txt", dtype=int)
            except OSError:
                continue
        else:
            A = np.random.randint(-10, 11, (N, N))

        if A.shape == (N, N):
            return A

def process_matrix(A):
    N = A.shape[0]
    h = N // 2
    F = A.copy()

    B = A[:h, :h]
    C = A[:h, h:]
    E = A[h:, h:]

    pos_even = np.sum(C[:, ::2] > 0)
    neg_odd = np.sum(C[:, 1::2] < 0)

    if pos_even > neg_odd:
        F[:h, :h] = np.fliplr(C)
        F[:h, h:] = np.fliplr(B)
    else:
        F[:h, h:], F[h:, h:] = E.copy(), C.copy()

    return F

def calculate(A, F, K):
    det_A = np.linalg.det(A)
    diag_F = np.trace(F)

    try:
        A_inv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Матрица A необратима"

    if det_A > diag_F:
        return A @ A.T - K * F @ A_inv
    else:
        G = np.tril(A)
        return (K * A_inv + G - F.T) * K

def plot_graphs(F):
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(F)
    plt.title("F")
    plt.colorbar()

    plt.subplot(1, 3, 2)
    plt.hist(F.flatten(), bins=15)
    plt.title("Histogram")

    plt.subplot(1, 3, 3)
    plt.plot(np.sum(F, axis=1), marker='o')
    plt.title("Row sums")

    plt.tight_layout()
    plt.show()

def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N (чётное): "))

    if N % 2 != 0:
        raise ValueError("N должно быть чётным")

    A = get_matrix(N)
    F = process_matrix(A)
    result = calculate(A, F, K)

    print("A:\n", A)
    print("F:\n", F)
    print("Результат:\n", result)

    plot_graphs(F)

if __name__ == "__main__":
    main()
