# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных


print('Задача 4: gользователь вводит 3 числа, сказать сколько из них положительных \n '
      'и сколько отрицательных')

max = 3
numbers = input('Enter any 3 numbers')
negative_numbers = numbers.count('-')
positive_numbers = max - negative_numbers
print(f'Negative number count = {negative_numbers} and positive = {positive_numbers}')
