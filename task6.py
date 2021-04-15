'''
Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об
отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
'''
goods = []
features = {'наименование': '', 'стоимость': '', 'количество': '', 'ед.из.': ''}
analytics = {'наименование': [], 'стоимость': [], 'количество': [], 'ед.из.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Выход '1', продолжить '2', собрать аналитику '3'").upper()
    if control == '1':
        break
    num += 1
    if control == '3':
        print(f'\n Аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
        continue
    if control == '2':
       print("Заполните поля, обратите внимание поля 'стоимость' и 'количество' должны быть целыми числами")
       for f in features.keys():

        try:
            feature_ = input(f'Введите "{f}"')
            features[f] = int(feature_) if (f == 'стоимость' or f == 'количество') else feature_
        except ValueError:
            print("Ошибка строка содержит не верный формат")
            break
        analytics[f].append(features[f])
    goods.append((num, features))
    print(features)
