'''
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def div(*args):

    try:
        arg1 = float(input("Введите первое число "))
        arg2 = float(input("Введите второе число "))
        res = arg1 / arg2
    except ValueError:
        return 'Не верный формат числа'
    except ZeroDivisionError:
        return "Не верно! Деление на 0 невозможно"

    return res



print(f'результат  {div()}')
