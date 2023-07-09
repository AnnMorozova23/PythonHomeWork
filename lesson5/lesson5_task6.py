# Дан список содержащий словари, в каждом словаре может быть или не быть ключ price.
# Значение ключа, при его наличии, является число (int, float).
# Необходимо рассчитать среднее значение price среди словарей у которых есть данный ключ.

some_dict_1 = {
    'price': 25,
    'name': 'book_1'
}

some_dict_2 = {
    'weight': 0.5,
    'name': 'book_2'
}

some_dict_3 = {
    'price': 45,
    'name': 'book_2'
}

books = [some_dict_1, some_dict_2, some_dict_3]

prices = []

for i in books:
    if i.get('price'):
        prices.append(i.get('price'))
result = sum(prices) / len(prices)
print(result)
