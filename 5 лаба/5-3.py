import itertools
import random

K = 10
T = 3

types = [random.randint(0, T - 1) for _ in range(K)]
skills = [random.randint(1, 10) for _ in range(K)]

def is_valid(trio):
    t = [types[i] for i in trio]
    return len(set(t)) == 3

def score(trio):
    return sum(skills[i] for i in trio)

best_trio = None
best_score = -1

for trio in itertools.combinations(range(K), 3):
    if is_valid(trio):
        s = score(trio)
        if s > best_score:
            best_score = s
            best_trio = trio

print("Лучшее трио:", best_trio)
print("Типы:", [types[i] for i in best_trio])
print("Навыки:", [skills[i] for i in best_trio])
print("Сумма:", best_score)
