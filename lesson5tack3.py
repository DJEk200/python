with open('sal.txt', 'r', encoding='UTF-8') as f:
    workers = {}
    sum = 0
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'зарплата меньше 20000 - у сотрудника {key}')
        sum += int(value)
        people = len(workers)
    wage_al = sum
    average_wage = wage_al / people
print(wage_al)
print(people)
print(f'{average_wage:.0f}')

