rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test_1.txt', 'r') as f:
    for i in f:
        i = i.split(' - ')
        new_file.append(rus[i[0]] + ' - ' + i[1])
    print(new_file)
with open('test_1_new.txt', 'w') as f_2:
    f_2.writelines(new_file)
