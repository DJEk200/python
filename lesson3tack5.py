def my_sum():
    end = True
    sum_result = 0

    while end:
        number = input('Введите числа через пробел или нажмите Q для выхода: ').upper()
        numbers = number.split()
        result = 0
        for elem in range(len(numbers)):
            if numbers[elem] == 'Q':
                end = False
                break
            else:
                result = result + int(numbers[elem])
        sum_result = sum_result + result
        print('Текущая сумма:', sum_result)
    print('Итоговая сумма:', sum_result)


my_sum()
