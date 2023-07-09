# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

some_list = [1, 5, 7, 8, 10, 15, 4, 8, 12, 3]
copy_list = some_list.copy()


def is_even(a):
    if a % 2 == 0:
        return True


some_list = list(filter(lambda x: is_even(x), some_list))
copy_list = list(filter(lambda x: not is_even(x), copy_list))

print(some_list + copy_list)
