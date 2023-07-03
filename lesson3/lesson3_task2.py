# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3

print('Задача 2: пользователь вводит 3 числа, найти среднее \n '
      'арифмитическое с точностью 3')

num1 = float(input('Enter number 1 = '))
num2 = float(input('Enter number 2 = '))
num3 = float(input('Enter number 3 = '))
index = 3
result = (num1 + num2 + num3) / index
print(round(result, 2))
