# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

n = 3
some_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = [6, 7, 8, 1, 2, 3, 4, 5] # это для меня тупенькой, чтоб я видела с чем сравнивать
result_2 = [4, 5, 6, 7, 8, 1, 2, 3] # это для меня тупенькой, чтоб я видела с чем сравнивать


def shift_list(some_list, n):
    if n > 0:
        step = len(some_list) - n
        return some_list[step:] + some_list[:step]
    else:
        n *= -1
        return some_list[n:] + some_list[:n]


print(shift_list(some_list, n))
