# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

n = int(input())
l = {}
total = 0
for i in range(1, n + 1):
    l[i] = int(round((1 + 1 / i) ** i, 0))
    total += l[i]
print(l, total)

