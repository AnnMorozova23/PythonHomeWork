# Вывести первые N цисел кратные M и больше K


K = 2
N = 5
count = 0
M = 5
while count < N:
    if K % M == 0:
        print(K)
        count += 1
    K += 1
