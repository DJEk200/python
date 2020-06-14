my_list = []
n = int(input("Введите число элементов, которое добавится в список: "))
x = 0
y = 1
for i in range(0, n):
    list_input = input()
    my_list.append(list_input)
print(my_list)
while y < n:
    my_list[x], my_list[y] = my_list[y], my_list[x]
    x += 2
    y += 2
print(my_list)
