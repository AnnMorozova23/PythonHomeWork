# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число


number_1 = float(input('Enter first number: '))
sign = input('Enter sign of operation (+,-, *, /): ')
number_2 = float(input('Enter second number: '))
result = 0

if sign == '+':
    result = number_1 + number_2
elif sign == '-':
    result = number_1 - number_2
elif sign == '*':
    result = number_1 * number_2
else:
    try:
        result = number_1 / number_2
    except ZeroDivisionError as e:
        print(f'Division by zero is not allowed: {e}')
print(result)
