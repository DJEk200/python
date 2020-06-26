import json
profit = {}
pr = {}
prof = 0
prof_average = 0
i = 0
with open('test_7.txt', 'r') as f:
    for line in f:
        name, firm, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = prof / i
        print(f'Средняя прибыль по фирмам составляет: {prof_average:.2f}')
    pr = {'Средняя прибыль по фирмам': round(prof_average)}
    profit.update(pr)
    print(f'Прибыль по каждой компании составляет: {profit}')

with open('file_7.json', 'w') as f_js:
    json.dump(profit, f_js)

    js_page = json.dumps(profit)
    print(js_page)