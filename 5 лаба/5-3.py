import itertools
import random
import time


# ==================================================
# Целевая функция
# Выбирает наиболее эффективный способ
# по минимальному времени выполнения
# ==================================================

def objective_function(time_algo, time_func):

    if time_algo < time_func:
        return "Алгоритмический способ"

    elif time_func < time_algo:
        return "Способ с помощью itertools"

    else:
        return "Оба способа работают одинаково"


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
# Ограничение:
# Берём только музыкантов
# с мастерством >= 5
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

print("\n=== Способ с помощью itertools ===")

for trio in trios_func:
    print(trio)

print(f"\nКоличество трио: {len(trios_func)}")
print(f"Время выполнения: {func_time:.6f} сек")


# ==================================================
# Использование целевой функции
# ==================================================

best_method = objective_function(
    algo_time,
    func_time
)


# ==================================================
# Сравнение способов
# ==================================================

print("\n=== Сравнение ===")

print(f"Оптимальный способ: {best_method}")
