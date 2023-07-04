# Заполнить список степенями числа 2 (от 2^1 до 2^n).


stop = int(input("Enter number: "))
start = 2
numbers = [start ** i for i in range(1, stop, 1)]
print(numbers)
