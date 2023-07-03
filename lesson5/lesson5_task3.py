# Вывести четные числа от 2 до N по 5 в строку

stop = int(input("Enter number: "))
count = 0
stat = 2
for i in range(stat, stop + 1):
    if i % 2 == 0:
        print(i)
        count += 1
        if count == 5:
            print()
            count = 0
