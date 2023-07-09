# Вывести четные числа от 2 до N по 5 в строку

stop = int(input("Enter number: "))
stat = 2
some_list = []
for i in range(stat, stop + 1, 2):
    some_list.append(i)

my_string = ' '.join(map(str, some_list))
my_string.split(None, maxsplit=5)
print(my_string)
