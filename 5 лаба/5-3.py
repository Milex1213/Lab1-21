import itertools
import random
import time


# ==================================================
# Целевая функция
# Ищет оптимальное решение:
# минимальное время + максимальное количество трио
# ==================================================

def objective_function(trios_count_algo,
                       trios_count_func,
                       time_algo,
                       time_func):

    print("\n=== Целевая функция ===")

    # Проверка корректности решений
    if trios_count_algo != trios_count_func:

        return (
            "Результаты различаются. "
            "Оптимальное решение определить нельзя."
        )

    # Поиск оптимального решения
    if time_algo < time_func:

        return (
            f"Оптимальное решение: "
            f"алгоритмический способ.\n"
            f"Количество трио: {trios_count_algo}\n"
            f"Время: {time_algo:.6f} сек"
        )

    elif time_func < time_algo:

        return (
            f"Оптимальное решение: "
            f"способ с itertools.\n"
            f"Количество трио: {trios_count_func}\n"
            f"Время: {time_func:.6f} сек"
        )

    else:

        return (
            f"Оба способа одинаково эффективны.\n"
            f"Количество трио: {trios_count_algo}"
        )


# ==================================================
# Ввод данных
# ==================================================

K = int(input("Введите количество музыкантов: "))
T = int(input("Введите количество типов инструментов: "))


# ==================================================
# Формирование музыкантов
# ==================================================

musicians = []

for i in range(K):

    instrument_type = (i % T) + 1
    skill = random.randint(1, 10)

    musicians.append(
        (i + 1, instrument_type, skill)
    )


# ==================================================
# Вывод музыкантов
# ==================================================

print("\nМузыканты:")

for m in musicians:
    print(
        f"Музыкант {m[0]} — "
        f"тип {m[1]} — "
        f"мастерство {m[2]}"
    )


# ==================================================
# Отбор музыкантов
# ==================================================

filtered_musicians = []

for m in musicians:

    if m[2] >= 5:
        filtered_musicians.append(m)


print("\nМузыканты, прошедшие отбор:")

for m in filtered_musicians:
    print(f"Музыкант {m[0]}")


# ==================================================
# Алгоритмический способ
# ==================================================

start1 = time.perf_counter()

trios_algo = []

N = len(filtered_musicians)

for i in range(N):

    for j in range(i + 1, N):

        for k in range(j + 1, N):

            trio = (
                filtered_musicians[i],
                filtered_musicians[j],
                filtered_musicians[k]
            )

            trios_algo.append(trio)

end1 = time.perf_counter()

algo_time = end1 - start1


print("\n=== Алгоритмический способ ===")

for trio in trios_algo:
    print(trio)

print(f"\nКоличество трио: {len(trios_algo)}")
print(f"Время выполнения: {algo_time:.6f} сек")


# ==================================================
# Способ с itertools
# ==================================================

start2 = time.perf_counter()

trios_func = list(
    itertools.combinations(
        filtered_musicians,
        3
    )
)

end2 = time.perf_counter()

func_time = end2 - start2


print("\n=== Способ с itertools ===")

for trio in trios_func:
    print(trio)

print(f"\nКоличество трио: {len(trios_func)}")
print(f"Время выполнения: {func_time:.6f} сек")


# ==================================================
# Нахождение оптимального решения
# ==================================================

result = objective_function(
    len(trios_algo),
    len(trios_func),
    algo_time,
    func_time
)

print(result)
