'''
А
'''
from itertools import count, cycle

x = int(input('Введите стартовое число: '))
y = int(input('Введите последнее число: '))
for i in count(start=x, step=1):
    if i > y:
        break
    print(i)

'''
 Б
'''

my_list = [1, 2.3, 'да', 'False']
с = 0
for elem in cycle(my_list):
    if с > 10000:
        break
    print(elem)
    с += 1
