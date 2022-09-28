# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Задайте список: '))
l = []
for i in range(-n, n + 1):
    l.append(i)
print(l)
random.shuffle(l)
print(l)
