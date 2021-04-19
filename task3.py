'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
'''
print("ведите три аргумента в виде любых целых чисел")
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
try:
    print(f'Сумма наибольших двух аргументов равна- {my_func(int(input("введите первый аргумент ")), int(input("введите второй аргумент ")), int(input("введите третий аргумент ")))}')
except ValueError:
    print("Ошибка! Вводимые данные должны быть целым числом")
