import itertools
import time

K = int(input("Введите количество музыкантов: "))
T = int(input("Введите количество типов инструментов: "))


musicians = []

for i in range(K):
    instrument_type = (i % T) + 1
    musicians.append((i + 1, instrument_type))

print("\nМузыканты:")
for m in musicians:
    print(f"Музыкант {m[0]} — инструмент типа {m[1]}")


# Алгоритмический способ формирования трио
start1 = time.perf_counter()

trios_algo = []

for i in range(K):
    for j in range(i + 1, K):
        for k in range(j + 1, K):
            trio = (musicians[i], musicians[j], musicians[k])
            trios_algo.append(trio)

end1 = time.perf_counter()

print("\n=== Алгоритмический способ ===")
for trio in trios_algo:
    print(trio)

print(f"\nКоличество трио: {len(trios_algo)}")
print(f"Время выполнения: {end1 - start1:.6f} сек")



# Способ с использованием функций Python
start2 = time.perf_counter()

trios_func = list(itertools.combinations(musicians, 3))

end2 = time.perf_counter()

print("\n=== Способ с помощью функций Python ===")
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

