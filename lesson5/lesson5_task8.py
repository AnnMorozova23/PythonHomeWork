# Дан список словарей, каждый словарь имеет ключи: category_id, title, price.
# Значение ключа category_id является целое положительное число, значением ключа name - str,
# а значение ключа price - float. Те словари, у которых ключ category_id = 1,
# необходимо удалить, а те у которых category_id = 2,
# необходимо уменьшить price на 5%. Остальные словари оставляем без изменений.


some_dict_1 = {
    'category_id': 1,
    'title': 'book_1',
    'price': 25.5
}

some_dict_2 = {
    'category_id': 2,
    'title': 'book_2',
    'price': 25.8
}

some_dict_3 = {
    'category_id': 3,
    'title': 'book_3',
    'price': 25.2
}

books = [some_dict_1, some_dict_2, some_dict_3]

for i in books:
    if i['category_id'] == 1:
        books.remove(i)
for i in books:
    if i['category_id'] == 2:
        new = i.get('price') * 0.95
        i['price'] = round(new, 2)
print(books)
