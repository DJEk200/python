import itertools
import math

n = int(input('Введите количество цифр на выведение: '))

def fact():
    for el in itertools.count(1):
        yield math.factorial(el)


x = 0
for el in fact():
    if x < n:
        print(el)
        x += 1
    else:
        break
