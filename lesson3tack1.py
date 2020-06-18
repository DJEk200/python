x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

def computation(x, y):

    try:
        res = x / y
    except ZeroDivisionError:
        return 'Деление на 0 запрещено, попробуйте заново'

    return res


print(computation(x, y))
