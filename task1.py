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

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''


print(f'результат  {div()}')