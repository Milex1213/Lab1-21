import itertools
import random
import time

K = int(input("Введите количество музыкантов: "))
T = int(input("Введите количество типов инструментов: "))


musicians = []

for i in range(K):
    instrument_type = (i % T) + 1
    skill = random.randint(1, 10)

    musicians.append((i + 1, instrument_type, skill))

print("\nМузыканты:")

for m in musicians:
    print(f"Музыкант {m[0]} — тип {m[1]} — мастерство {m[2]}")

# Ограничение:
# В перебор включаются только музыканты
# с уровнем мастерства >= 5

filtered_musicians = []

for m in musicians:
    if m[2] >= 5:
        filtered_musicians.append(m)

print("\nМузыканты, прошедшие отбор:")

for m in filtered_musicians:
    print(f"Музыкант {m[0]}")

# Алгоритмический способ

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

print("\n=== Алгоритмический способ ===")

for trio in trios_algo:
    print(trio)

print(f"\nКоличество трио: {len(trios_algo)}")
print(f"Время выполнения: {end1 - start1:.6f} сек")

# Способ с помощью itertools

start2 = time.perf_counter()

trios_func = list(itertools.combinations(filtered_musicians, 3))

end2 = time.perf_counter()

print("\n=== Способ с помощью itertools ===")

for trio in trios_func:
    print(trio)

print(f"\nКоличество трио: {len(trios_func)}")
print(f"Время выполнения: {end2 - start2:.6f} сек")

# Сравнение времени

print("\n=== Сравнение ===")

if (end1 - start1) < (end2 - start2):
    print("Алгоритмический способ быстрее.")
elif (end1 - start1) > (end2 - start2):
    print("Способ с itertools быстрее.")
else:
    print("Время выполнения одинаковое.")

