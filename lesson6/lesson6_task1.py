# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def convert_function(a):
    binary = []
    while a > 0:
        i = a % 2
        binary.insert(0, i)
        a = a // 2
    print(f'binary system: ', binary)

    step = 0
    number = 0
    for i in binary[::-1]:
        if i == 0:
            number = number + 0
        else:
            number += 2 ** step
        step += 1
    print(f'decimal system: ', number)


convert_function(100)
