# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input())
n = int(str(n).replace('.', ''))
summ = 0
while n % 10 != 0:
    n *= 10
while n > 0:
    b = n % 10
    summ += b
    n //= 10
print(summ)
