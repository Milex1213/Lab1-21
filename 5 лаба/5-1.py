import time

K = 10
musicians = list(range(K))

start = time.time()

trios_algo = []
for i in range(K):
    for j in range(i + 1, K):
        for k in range(j + 1, K):
            trios_algo.append((musicians[i], musicians[j], musicians[k]))

end = time.time()

print("Алгоритмический способ:")
print("Количество трио:", len(trios_algo))
print("Время:", end - start)
