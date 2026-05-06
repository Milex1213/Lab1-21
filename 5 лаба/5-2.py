import time
import itertools

K = 10
musicians = list(range(K))

start = time.time()

trios_func = list(itertools.combinations(musicians, 3))

end = time.time()

print("Функциональный способ:")
print("Количество трио:", len(trios_func))
print("Время:", end - start)
