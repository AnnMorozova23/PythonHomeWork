# # Вводится число N, необходимо вывести N чисел Фибоначчи
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

N = int(input('Enter N: '))
result = []
a = 0
b = 1
while len(result) < N:
    result.append(a)
    prev = a
    a = b
    b = prev + a
print(result)
