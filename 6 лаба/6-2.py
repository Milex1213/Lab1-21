import timeit
import matplotlib.pyplot as plt


# Функция вычисления факториала
def factorial(x):

    result = 1

    for i in range(2, x + 1):
        result *= i

    return result


# Рекурсивный метод
def F_recursive(n, memo=None):

    if memo is None:
        memo = {}

    # Базовые случаи
    if n == 0:
        return 5

    if n == 1:
        return 1

    # Проверка, вычислялось ли значение ранее
    if n not in memo:

        # Знак (-1)^n
        sign = -1 if n % 2 else 1

        memo[n] = sign * (
            2 * F_recursive(n - 1, memo) / factorial(n) +
            F_recursive(n - 2, memo) / factorial(2 * n)
        )

    return memo[n]


# Итерационный метод
def F_iterative(n):

    # Базовые случаи
    if n == 0:
        return 5

    if n == 1:
        return 1

    # Начальные значения
    prev2 = 5      # F(0)
    prev1 = 1      # F(1)

    # Начальные факториалы:
    # 1! = 1
    # 2! = 2
    fact_n = 1
    fact_2n = 2

    for i in range(2, n + 1):

        # Обновление n!
        # i! = (i-1)! * i
        fact_n *= i

        # Обновление (2i)!
        # (2i)! = (2i-2)! * (2i-1) * (2i)
        fact_2n *= (2 * i - 1) * (2 * i)

        # Знак (-1)^i
        sign = -1 if i % 2 else 1

        # Вычисление текущего значения
        current = sign * (
            2 * prev1 / fact_n +
            prev2 / fact_2n
        )

        # Сдвиг значений
        prev2 = prev1
        prev1 = current

    return prev1


# Сравнение времени выполнения
def compare_methods(max_n):

    recursive_times = []
    iterative_times = []

    results = []

    for n in range(max_n + 1):

        # Время рекурсивного метода
        rec_time = timeit.timeit(
            lambda: F_recursive(n),
            number=1000
        ) / 1000

        # Время итерационного метода
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


# Вывод таблицы результатов
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


# Построение графика
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


# Главная функция
def main():

    max_n = 20

    recursive_times, iterative_times, results = compare_methods(max_n)

    print_table(results)

    show_plot(
        recursive_times,
        iterative_times,
        max_n
    )


if __name__ == "__main__":
    main()
