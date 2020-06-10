print('Введите приход денежных средств')
coming = int(input())
print('Введите расход денежных средств')
outlay = int(input())
profit = coming - outlay
profitability = profit / coming * 100
if outlay > coming:
    print('Вы работаете в убыток')
elif outlay < coming:
    print('Вы работаете в прибыль')
    print('Рентабельность составляет', profitability, '%')
    print('Введите количество сотрудников')
    people = int(input())
    profit_company_for_people = profit / people
    print('Прибыль в расчете на человека составляет', profit_company_for_people)
else:
    print('Вы работаете без прибыли и без убытка')