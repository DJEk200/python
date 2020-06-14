my_list = input('Введите слова через пробел: ')
my_list = my_list.split()
x = 0
y = len(my_list)
while x < y:
    if len(my_list[x]) > 10:
        print(x + 1, my_list[x][:10])
    else:
        print(x + 1, my_list[x])
    x += 1
