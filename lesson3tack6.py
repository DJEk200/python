def int_func(some_string):
    result = some_string.title()
    return result


string = input('Введите слово c маленькой буквы: ')
print(f"Было: {string}")
print(f'Стало: {int_func(string)}')
