# Вводится число, необходимо подсчитать его факториал


N = int(input('Enter num: '))
stop = N + 1
result = 0
count = 1
for i in range(1, stop):
    result = i * count
    count += 1
    count = result
print(result)
