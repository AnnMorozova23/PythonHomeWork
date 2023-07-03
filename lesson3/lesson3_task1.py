# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способам

print('Задача 1: Пользователь вводит предложение, заменить все \n'
      ' пробелы на "-" 2-мя способам')
input_text = input("Input some words using 'space' : ")
print(input_text.replace(' ', '-'))
input_text1 = '-'.join(input_text.split(' '))
print(input_text1)
