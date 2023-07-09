# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

some_list = [1, 2, 3, 4, 5, 6, 7, 8]
left = -1
right = -len(some_list) + 1
index = 0


def sum_function_neighbours(some_list, left, right, index):
    result_list = []
    while index < len(some_list):
        result_list.append(some_list[left] + some_list[right])
        left += 1
        right += 1
        index += 1
    return result_list


print(sum_function_neighbours(some_list, left, right, index))
