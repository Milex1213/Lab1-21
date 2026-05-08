import itertools
import random
import time


# ==================================================
# Целевая функция
# Поиск оптимального трио
# по максимальному среднему мастерству
# ==================================================

def objective_function(trios):

    best_trio = None
    best_average_skill = 0

    for trio in trios:

        # Сумма мастерства трио
        total_skill = (
            trio[0][2] +
            trio[1][2] +
            trio[2][2]
        )

        # Среднее мастерство
        average_skill = total_skill / 3

        # Поиск максимального значения
        if average_skill > best_average_skill:

            best_average_skill = average_skill
            best_trio = trio

    return best_trio, best_average_skill


# ==================================================
# Ввод данных
# ==================================================

K = int(input("Введите количество музыкантов: "))
T = int(input("Введите количество типов инструментов: "))


# ==================================================
# Формирование списка музыкантов
# ==================================================

musicians = []

for i in range(K):

    instrument_type = (i % T) + 1

    # Случайный уровень мастерства
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


# ==================================================
# Вывод алгоритмического способа
# ==================================================

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


# ==================================================
# Вывод способа itertools
# ==================================================

print("\n=== Способ с itertools ===")

for trio in trios_func:
    print(trio)

print(f"\nКоличество трио: {len(trios_func)}")
print(f"Время выполнения: {func_time:.6f} сек")


# ==================================================
# Поиск оптимального трио
# ==================================================

best_trio, best_average = objective_function(trios_func)


# ==================================================
# Вывод оптимального решения
# ==================================================

print("\n=== Оптимальное трио ===")

print("Лучшее трио:")

for musician in best_trio:

    print(
        f"Музыкант {musician[0]} — "
        f"тип {musician[1]} — "
        f"мастерство {musician[2]}"
    )

print(f"\nСреднее мастерство трио: {best_average:.2f}")
