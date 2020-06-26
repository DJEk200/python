with open("text.txt", 'w') as f:
    while True:
        text_in = input('Введите текст: ')
        if text_in == '':
            print('Ввод окончен')
            f.close()
            exit()
        else:
            f.write(text_in + '\n')
