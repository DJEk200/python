def total():
    try:
        with open('test_5.txt', 'w+') as f:
            line = input('Введите цифры через пробел: ')
            f.writelines(line)
            my_file = line.split()
            print(sum(map(int, my_file)))
    except ValueError:
        print('Вы ввели не цифровое значение, попробуйте еще раз!')
total()