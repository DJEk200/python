my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [elem for num, elem in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список:\n{my_list}')
print(f'Новый список:\n{new_list}')
