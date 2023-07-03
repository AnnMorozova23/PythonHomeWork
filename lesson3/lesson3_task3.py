# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

print('Задача 3: пользователь вводит Имя, Возраст и Город, сформировать \n '
      'приветственное сообщение путем форматирования 3-мя способами')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter your  city: ')
print('Hello %s your age is %d and your city is %s' % (name, age, city))
print('Hello {} your age is {} and your city is {}'.format(name, age, city))
print(f'Hello {name} your age is {age} and your city is {city}')
