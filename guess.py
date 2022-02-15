"""Игра компьютер угадывает число за 20 попыток"""

import numpy as np
min = 1
max = 101

number = np.random.randint(min, max) # предполагаемое число

count = 0

while True:
    count += 1
    exp = round((min+max) / 2) # разбиваем пополам,новые рамки поиска
    
    if exp > number:
        max = exp
    
    elif exp < number:
        min = exp

    else:
        print("attempt {} . number {}".format(count, number))
        break #конец игры выход из цикла.

     