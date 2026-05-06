# Лабораторная работа
# F(0) = 5; F(1) = 1;
# F(n) = (-1)^n * ( 2F(n-1)/n! + F(n-2)/(2n)! )

import timeit
import matplotlib.pyplot as plt

# --- РЕКУРСИЯ С МЕМОИЗАЦИЕЙ ---
def F_recursive(n, memo={}):
    if n == 0:
        return 5
    if n == 1:
        return 1

    if n not in memo:
        factorial_n = calculate_factorial(n)
        factorial_2n = calculate_factorial(2 * n)

        memo[n] = ((-1) ** n) * (
            2 * F_recursive(n - 1, memo) / factorial_n +
            F_recursive(n - 2, memo) / factorial_2n
        )

    return memo[n]


# --- ИТЕРАЦИЯ (ОПТИМИЗИРОВАННАЯ) ---
def F_iterative_optimized(n):
    if n == 0:
        return 5
    if n == 1:
        return 1

    prev2 = 5   # F(0)
    prev1 = 1   # F(1)

    fact_n = 1
    fact_2n = 1

    for i in range(1, 2 * n + 1):
        fact_2n *= i
        if i == n:
            fact_n = fact_2n

    for i in range(2, n + 1):
        factorial_n = calculate_factorial(i)
        factorial_2n = calculate_factorial(2 * i)

        current = ((-1) ** i) * (
            2 * prev1 / factorial_n +
            prev2 / factorial_2n
        )

        prev2, prev1 = prev1, current

    return prev1


# --- ФАКТОРИАЛ ---
def calculate_factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


# --- СРАВНЕНИЕ ---
def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    results = []

    for n in range(0, max_n + 1):
        # рекурсия
        recursive_timer = timeit.Timer(lambda: F_recursive(n))
        recursive_time = recursive_timer.timeit(number=1)
        recursive_times.append(recursive_time)

        # итерация
        iterative_timer = timeit.Timer(lambda: F_iterative_optimized(n))
        iterative_time = iterative_timer.timeit(number=1)
        iterative_times.append(iterative_time)

        # значения
        rec_val = F_recursive(n)
        iter_val = F_iterative_optimized(n)

        results.append((n, rec_val, iter_val))

    return recursive_times, iterative_times, results


# --- MAIN ---
def main():
    max_n = 15

    recursive_times, iterative_times, results = compare_methods(max_n)

    print("Таблица результатов:")
    print("n | Рекурсивное значение | Итеративное значение | Время рекурсии | Время итерации")
    print("-" * 90)

    for i, (n, rec_val, iter_val) in enumerate(results):
        print(f"{n:2d} | {rec_val:<20.10f} | {iter_val:<20.10f} | {recursive_times[i]:.6f} | {iterative_times[i]:.6f}")

    # --- ГРАФИК ---
    plt.figure(figsize=(10, 5))
    plt.plot(range(0, max_n + 1), recursive_times, label='Рекурсивный метод')
    plt.plot(range(0, max_n + 1), iterative_times, label='Итеративный метод')

    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение методов')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
