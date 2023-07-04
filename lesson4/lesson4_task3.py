# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input("Enter n: "))

some_dict = {}
for i in range(n + 1):
    name = input(f'Enter name for key {i}: ')
    email = input(f'Enter email for key{i}: ')
    some_dict[i] = {"name": name, "email": email}
print(some_dict)
print(some_dict.values())
