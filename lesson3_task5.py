# Есть процент, есть сумма, через сколько лет сумма удвоится, учесть банковскую капитализацию (сложные проценты)
import math

first_sum = float(input('Enter sum of deposit: '))
rate = float(input('Enter interest rate: '))
base = 1 + (rate / 100)  # Основание логарифма
result_sum = first_sum * 2  # Удвоенна сумма в конце периода
number = result_sum / first_sum  # Число логарифма
period = round(math.log(number, base),
               0)  # Вычисляем степень (количество лет) с помощью логарифма S = P*(1+ i)^n -> (1+i)^n = S/P -> log1+i(S/P)
print(f'Сумма {first_sum} удвоится через {period} лет при ставке в {rate}% ')
