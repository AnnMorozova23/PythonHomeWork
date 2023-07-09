# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

some_list = [1, 2, 3, 4, 5, 6, 7]
result = [7, 6, 5, 4, 3, 2, 1]
n = len(some_list) - 1
start = 0


def reversed_function(some_list, n, start):
    while start < n:
        some_list[start] = some_list[n]
        some_list[n] = some_list[start]
        start += 1
        n -= 1


print(some_list)

reversed_function(some_list, n, start)
