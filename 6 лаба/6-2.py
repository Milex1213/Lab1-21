import timeit
import matplotlib.pyplot as plt


def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


def F_recursive(n, memo=None):

    if memo is None:
        memo = {}

    if n == 0:
        return 5

    if n == 1:
        return 1

    if n not in memo:

        memo[n] = ((-1) ** n) * (
            2 * F_recursive(n - 1, memo) / factorial(n) +
            F_recursive(n - 2, memo) / factorial(2 * n)
        )

    return memo[n]


def F_iterative(n):

    if n == 0:
        return 5

    if n == 1:
        return 1

    prev2, prev1 = 5, 1
    fact_n, fact_2n = 1, 1
    current_n, current_2n = 1, 1

    for i in range(2, n + 1):

        while current_n < i:
            current_n += 1
            fact_n *= current_n

        while current_2n < 2 * i:
            current_2n += 1
            fact_2n *= current_2n

        current = ((-1) ** i) * (
            2 * prev1 / fact_n +
            prev2 / fact_2n
        )

        prev2, prev1 = prev1, current

    return prev1


def compare_methods(max_n):

    recursive_times = []
    iterative_times = []
    results = []

    for n in range(max_n + 1):

        rec_time = timeit.timeit(
            lambda: F_recursive(n),
            number=1000
        ) / 1000

        iter_time = timeit.timeit(
            lambda: F_iterative(n),
            number=1000
        ) / 1000

        recursive_times.append(rec_time)
        iterative_times.append(iter_time)

        results.append((
            n,
            F_recursive(n),
            F_iterative(n),
            rec_time,
            iter_time
        ))

    return recursive_times, iterative_times, results


def print_table(results):

    print("\nТаблица результатов\n")

    header = (
        f"{'n':^5}"
        f"{'Рекурсивное значение':^28}"
        f"{'Итеративное значение':^28}"
        f"{'Время рекурсии (с)':^24}"
        f"{'Время итерации (с)':^24}"
    )

    print(header)
    print("-" * len(header))

    for n, rec_val, iter_val, rec_time, iter_time in results:

        print(
            f"{n:^5}"
            f"{rec_val:^28.10f}"
            f"{iter_val:^28.10f}"
            f"{rec_time:^24.10f}"
            f"{iter_time:^24.10f}"
        )


def show_plot(recursive_times, iterative_times, max_n):

    plt.figure(figsize=(10, 5))

    plt.plot(
        range(max_n + 1),
        recursive_times,
        marker='o',
        label='Рекурсивный метод'
    )

    plt.plot(
        range(max_n + 1),
        iterative_times,
        marker='s',
        label='Итеративный метод'
    )

    plt.xlabel('n')
    plt.ylabel('Среднее время выполнения (с)')
    plt.title('Сравнение времени вычисления')

    plt.legend()
    plt.grid(True)
    plt.show()


def main():

    max_n = 20

    recursive_times, iterative_times, results = compare_methods(max_n)

    print_table(results)
    show_plot(recursive_times, iterative_times, max_n)


if __name__ == "__main__":
    main()
