goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для ввода нажмите 'Enter' ").upper()
    if control == 'Q':
        break
    num += 1
    for f in features.keys():
        feature_ = input(f'Введите "{f}" ')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
print(f'\nАналитика склада')
for key, value in analytics.items():
    print(f'{key}: {value}')

