# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

some_string = input('enter some words: ')
helper = list(some_string)
value = {i: helper.count(i) for i in helper}
print(value)


