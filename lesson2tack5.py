my_list = [7, 5, 3, 3, 2]
x = int(input('Введите число рейтинга от 1 до 9: '))
my_list.append(x)
y = sorted(my_list, reverse=True)
print(y)
