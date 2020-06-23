def wage():
    try:
        time = float(input('Отработанное количество часов: '))
        salary = int(input('Стоимость 1 часа работы: '))
        if time > 50:
            bonus = salary * 1.1
            res = time * salary + bonus
            print(f'Сотруднику к начислению положено: {res}')
        else:
            res = time * salary
            print(f'Сотруднику к начислению положено: {res}')
    except ValueError:
        return print('Вы ввели не число, попробуйте заново')
wage()
