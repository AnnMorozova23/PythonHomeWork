# Вывести первые N цисел кратные M и больше K

K = 5
N = 100
i = 0
M = 5
for i in range(N):
    if i % M == 0 and i > K:
        print(i)
