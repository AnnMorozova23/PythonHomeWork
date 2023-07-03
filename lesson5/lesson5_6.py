# Вводится число, необходимо проверить является ли оно простым


n = 18
counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        counter += 1
print(f'Simple' if counter == 2 else 'not simple')
