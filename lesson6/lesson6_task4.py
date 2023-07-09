# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

some_list = ['test', [4, 5, 'f'], 5, 'test2']
some_list = list(filter(lambda i: isinstance(i, str), some_list))
print(some_list)

